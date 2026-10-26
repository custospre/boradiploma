import re, html, sys
from html.parser import HTMLParser

BLOCK = {'p','div','br','tr','li','h1','h2','h3','h4','h5','h6','table','blockquote','center','td','dd','dt'}
SKIP = {'script','style','head','title'}
STRIKE = {'strike','s','del'}

def norm(t): return re.sub(r'\s+',' ',t.replace('\xa0',' ')).strip()

class P(HTMLParser):
    """Separa o texto em blocos; para cada bloco guarda (texto visível, texto riscado)."""
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out=[]; self.cur=[]; self.scur=[]; self.skip=0; self.strike=0
    def flush(self):
        t=norm(''.join(self.cur)); st=norm(''.join(self.scur)); self.cur=[]; self.scur=[]
        if t or st: self.out.append((t,st))
    def handle_starttag(self,tag,attrs):
        if tag in SKIP: self.skip+=1
        elif tag in STRIKE: self.strike+=1
        elif tag in BLOCK: self.flush()
    def handle_endtag(self,tag):
        if tag in SKIP: self.skip=max(0,self.skip-1)
        elif tag in STRIKE: self.strike=max(0,self.strike-1)
        elif tag in BLOCK: self.flush()
    def handle_startendtag(self,tag,attrs):
        if tag in BLOCK: self.flush()
    def handle_data(self,d):
        if self.skip: return
        if self.strike: self.scur.append(d)
        else: self.cur.append(d)

def decode(b):
    if b[:2] in (b'\xff\xfe', b'\xfe\xff'): return b.decode('utf-16',errors='replace')
    if b[:3]==b'\xef\xbb\xbf': return b[3:].decode('utf-8',errors='replace')
    m=re.search(rb'charset\s*=\s*["\']?([\w-]+)',b[:3000],re.I)
    enc=(m.group(1).decode() if m else 'windows-1252').lower()
    if enc in ('iso-8859-1','latin1','latin-1'): enc='windows-1252'
    try: return b.decode(enc)
    except Exception:
        try: return b.decode('utf-8')
        except Exception: return b.decode('windows-1252',errors='replace')

def strike_spans(t):
    # <span style="text-decoration: line-through">...</span> -> <strike>...</strike>
    return re.sub(r'<span[^>]*line-through[^>]*>(.*?)</span>',r'<strike>\1</strike>',t,flags=re.I|re.S)

# "Art. 1º", "Art . 1º", "Art. 1o-A", "Art. 12-B." ; o sufixo (-A) precisa vir colado ao número
# (assim "Art. 1º - A execução..." NÃO vira artigo 1-A)
ART=re.compile(r'^Art\s*\.?\s*(\d{1,4}(?:\.\d{3})?)(?:\s*[ºo°])?(?:-([A-Z]{1,2})(?![A-Za-zÀ-ú]))?\s*\.?',re.I)
REF=re.compile(r'\((?:Reda[çc][ãa]o|Inclu[íi]d|Revogad|Vide|Vig[êe]ncia|Renumerad|Acrescid|Regulamento|Promulga|Produ[çc][ãa]o de efeito|Vetad|Express[ãa]o|Declarad|Suprimid|Alterad|Com reda|Revoga)[^()]*(?:\([^()]*\)[^()]*)*\)',re.I)
END=re.compile(r'^(Bras[íi]lia|Rio de Janeiro|Este texto n[ãa]o substitui)',re.I)

def esc(s): return html.escape(s,quote=False)

def convert(raw, code, sub):
    t=strike_spans(decode(raw))
    p=P(); p.feed(t); p.flush()
    paras=[]
    for vis,st in p.out:
        v2=(vis or '').lstrip(' .;,:-')
        onlyref = (not v2) or not REF.sub('',v2).strip(' .;,:-')
        m=ART.match(st) if st else None
        if onlyref and m and not ART.match(vis or ''):
            note=v2 if (v2 and REF.search(v2)) else '(Revogado)'
            paras.append((st[:m.end()].strip()+' '+note, True))
        elif vis:
            paras.append((vis, False))
    start=None
    for i,(x,rev) in enumerate(paras):
        m=ART.match(x)
        if m and m.group(1)=='1' and not m.group(2): start=i; break
    if start is None: raise Exception('sem Art. 1')
    arts=[]; seen={}; last=0
    for x,rev in paras[start:]:
        if END.match(x): break
        m=ART.match(x)
        if m:
            num=int(m.group(1).replace('.','')); suf=(m.group(2) or '').lower()
            key=str(num)+('-'+suf if suf else '')
            if rev and not (last < num <= last+15 or (num==last and suf)):
                continue
            # número fora de sequência = artigo de OUTRA lei citado no texto -> fica como parágrafo do artigo atual
            if not rev and last and (num > last+15 or num < last):
                if arts: arts[-1]['paras'].append(x)
                continue
            if arts and arts[-1]['rev'] and arts[-1]['n']==key:
                old=arts.pop(); seen[old['id']]=seen.get(old['id'],0)-1
                if seen[old['id']]<0: del seen[old['id']]
            aid=code+'-art-'+key
            if aid in seen: seen[aid]+=1; aid=aid+'-r'+str(seen[aid])
            else: seen[aid]=0
            arts.append({'id':aid,'n':key,'paras':[x],'rev':rev})
            last=max(last,num)
        elif arts and not rev:
            arts[-1]['paras'].append(x)
    out=[f'<section class="code" id="code-{code}" data-code="{code}">',
         f'<p class="sub">{esc(sub)} — texto compilado. Fonte: Planalto.</p>',
         f'<div id="empty-{code}" class="emptybox" hidden>Artigo não encontrado neste diploma.</div>']
    for a in arts:
        out.append(f'<article id="{a["id"]}" data-n="{a["n"]}">')
        for j,x in enumerate(a['paras']):
            h=esc(x)
            h=REF.sub(lambda mm:'<span class="ref">'+mm.group(0)+'</span>',h)
            if j==0:
                m=ART.match(x); lab=esc(x[:m.end()])
                if h.startswith(lab): h='<span class="anum">'+lab+'</span>'+h[len(lab):]
            out.append('<p>'+h+'</p>')
        out.append('</article>')
    out.append('</section>')
    nums=[int(re.match(r'\d+',a['n']).group()) for a in arts if '-r' not in a['id']]
    return '\n'.join(out), len(arts), (max(nums) if nums else 0)

if __name__=='__main__':
    raw=open(sys.argv[1],'rb').read()
    s,n,mx=convert(raw,sys.argv[2],sys.argv[3])
    open(sys.argv[4],'w',encoding='utf-8').write(s)
    print(n,'artigos, maior nº',mx,',',len(s),'bytes')
