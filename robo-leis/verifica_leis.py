# -*- coding: utf-8 -*-
# Robo que DETECTA (sem alterar nada) quais leis do Planalto mudaram em relacao a uma "foto" (baseline).
# Escreve 'mudancas.txt' (vazio se nada mudou) e atualiza 'baseline_leis.json'.
import re, json, os, sys, hashlib, subprocess, html as H

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from laws import LAWS
import conv

BASELINE = os.path.join(HERE, "baseline_leis.json")
SAIDA = os.path.join(HERE, "mudancas.txt")


def plain(section_html):
    t = re.sub(r'<[^>]+>', ' ', section_html)
    t = H.unescape(t)
    return re.sub(r'\s+', ' ', t).strip()


def fetch(url):
    r = subprocess.run(
        ['curl', '-sS', '-m', '90', '-A',
         'Mozilla/5.0 (Windows NT 10.0; Win64; x64)', url],
        capture_output=True)
    if r.returncode != 0 or not r.stdout:
        raise Exception('download falhou: ' + r.stderr.decode(errors='replace')[:160])
    return r.stdout


def main():
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else 999999
    base = json.load(open(BASELINE, encoding='utf-8')) if os.path.exists(BASELINE) else {}
    novo = dict(base)
    mudaram, suspeitos, erros, cont = [], [], [], 0
    for area, items in LAWS:
        for code, name, sub, url, exp in items:
            if cont >= limit:
                break
            cont += 1
            try:
                raw = fetch(url)
                s, n, mx = conv.convert(raw, code, sub)
                L = len(plain(s))
                fp = hashlib.sha256(plain(s).encode('utf-8')).hexdigest()
                reg = {"fp": fp, "n": n, "len": L}
                old = base.get(code)
                if not isinstance(old, dict):
                    print(f'{code:9} foto inicial ({n} arts)')
                    novo[code] = reg
                elif old.get("fp") == fp:
                    print(f'{code:9} igual')
                elif L < old.get("len", 0) * 0.5 or n < max(3, old.get("n", 0) * 0.5):
                    suspeitos.append((code, name))
                    print(f'{code:9} SUSPEITO (texto muito menor; possivel erro de download)')
                    # NAO atualiza a foto, pra nao perder a boa
                else:
                    mudaram.append((code, name))
                    novo[code] = reg
                    print(f'{code:9} *** MUDOU ***')
            except Exception as e:
                erros.append((code, str(e)))
                print(f'{code:9} ERRO: {e}')
        if cont >= limit:
            break

    json.dump(novo, open(BASELINE, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)

    linhas = []
    if mudaram:
        linhas.append("Estas leis parecem ter MUDADO no Planalto. Confira e, se confirmar, peça para atualizar no app:\n")
        for _, nm in mudaram:
            linhas.append(f"- {nm}")
    if suspeitos:
        linhas.append("\nSuspeitas (o texto veio menor que o normal, pode ser erro de download) — verificar manualmente:")
        for _, nm in suspeitos:
            linhas.append(f"- {nm}")
    open(SAIDA, 'w', encoding='utf-8').write("\n".join(linhas))

    print('\n=== RESUMO ===')
    print('mudaram:', [c for c, _ in mudaram])
    print('suspeitos:', [c for c, _ in suspeitos])
    print('erros:', erros)


if __name__ == '__main__':
    main()
