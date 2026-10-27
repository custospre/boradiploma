# área -> lista de (código, nome curto, descrição oficial, URL do Planalto, nº do último artigo esperado)
B='https://www.planalto.gov.br/ccivil_03/'
LAWS = [
 ('Administrativa', [
  ('licit',  'Licitações e Contratos (Lei 14.133/2021)', 'Lei nº 14.133, de 1º de abril de 2021', B+'_ato2019-2022/2021/lei/l14133.htm', 194),
  ('improb', 'Improbidade Administrativa (Lei 8.429/1992)', 'Lei nº 8.429, de 2 de junho de 1992', B+'leis/l8429.htm', 25),
  ('procadm','Processo Administrativo Federal (Lei 9.784/1999)', 'Lei nº 9.784, de 29 de janeiro de 1999', B+'leis/l9784.htm', 70),
  ('servpub','Servidores Públicos Federais (Lei 8.112/1990)', 'Lei nº 8.112, de 11 de dezembro de 1990', B+'leis/l8112cons.htm', 253),
 ]),
 ('Ambiental', [
  ('crimamb','Crimes Ambientais (Lei 9.605/1998)', 'Lei nº 9.605, de 12 de fevereiro de 1998', B+'leis/l9605.htm', 82),
  ('pnma',   'Política Nacional do Meio Ambiente (Lei 6.938/1981)', 'Lei nº 6.938, de 31 de agosto de 1981', B+'leis/l6938.htm', 21),
  ('flor',   'Código Florestal (Lei 12.651/2012)', 'Lei nº 12.651, de 25 de maio de 2012', B+'_ato2011-2014/2012/lei/l12651.htm', 84),
 ]),
 ('Civil', [
  ('lindb',  'LINDB (Decreto-Lei 4.657/1942)', 'Decreto-Lei nº 4.657, de 4 de setembro de 1942 — Lei de Introdução às Normas do Direito Brasileiro', B+'decreto-lei/del4657compilado.htm', 30),
  ('inquil', 'Lei do Inquilinato (Lei 8.245/1991)', 'Lei nº 8.245, de 18 de outubro de 1991', B+'leis/l8245.htm', 90),
  ('bemfam', 'Bem de Família (Lei 8.009/1990)', 'Lei nº 8.009, de 29 de março de 1990', B+'leis/l8009.htm', 8),
  ('regpub', 'Registros Públicos (Lei 6.015/1973)', 'Lei nº 6.015, de 31 de dezembro de 1973', B+'leis/l6015compilada.htm', 299),
  ('alim',   'Lei de Alimentos (Lei 5.478/1968)', 'Lei nº 5.478, de 25 de julho de 1968', B+'leis/l5478.htm', 29),
 ]),
 ('Comercial', [
  ('cheque', 'Lei do Cheque (Lei 7.357/1985)', 'Lei nº 7.357, de 2 de setembro de 1985', B+'leis/l7357.htm', 71),
  ('dupl',   'Lei das Duplicatas (Lei 5.474/1968)', 'Lei nº 5.474, de 18 de julho de 1968', B+'leis/l5474.htm', 28),
 ]),
 ('Eleitoral', [
  ('eleicoes','Lei das Eleições (Lei 9.504/1997)', 'Lei nº 9.504, de 30 de setembro de 1997', B+'leis/l9504.htm', 107),
  ('inelegib','Lei de Inelegibilidade (LC 64/1990)', 'Lei Complementar nº 64, de 18 de maio de 1990', B+'leis/lcp/lcp64.htm', 28),
  ('partidos','Partidos Políticos (Lei 9.096/1995)', 'Lei nº 9.096, de 19 de setembro de 1995', B+'leis/l9096.htm', 63),
 ]),
 ('Empresarial', [
  ('falen',  'Falência e Recuperação de Empresas (Lei 11.101/2005)', 'Lei nº 11.101, de 9 de fevereiro de 2005', B+'_ato2004-2006/2005/lei/l11101.htm', 201),
  ('sa',     'Sociedades Anônimas (Lei 6.404/1976)', 'Lei nº 6.404, de 15 de dezembro de 1976', B+'leis/l6404consol.htm', 300),
 ]),
 ('Internacional', [
  ('migra',  'Lei de Migração (Lei 13.445/2017)', 'Lei nº 13.445, de 24 de maio de 2017', B+'_ato2015-2018/2017/lei/l13445.htm', 125),
 ]),
 ('Penal', [
  ('contrav','Contravenções Penais (Decreto-Lei 3.688/1941)', 'Decreto-Lei nº 3.688, de 3 de outubro de 1941', B+'decreto-lei/del3688.htm', 72),
  ('lep',    'Execução Penal (Lei 7.210/1984)', 'Lei nº 7.210, de 11 de julho de 1984', B+'leis/l7210.htm', 204),
  ('hedi',   'Crimes Hediondos (Lei 8.072/1990)', 'Lei nº 8.072, de 25 de julho de 1990', B+'leis/l8072.htm', 13),
  ('drogas', 'Lei de Drogas (Lei 11.343/2006)', 'Lei nº 11.343, de 23 de agosto de 2006', B+'_ato2004-2006/2006/lei/l11343.htm', 75),
  ('mpenha', 'Lei Maria da Penha (Lei 11.340/2006)', 'Lei nº 11.340, de 7 de agosto de 2006', B+'_ato2004-2006/2006/lei/l11340.htm', 46),
  ('abuso',  'Abuso de Autoridade (Lei 13.869/2019)', 'Lei nº 13.869, de 5 de setembro de 2019', B+'_ato2019-2022/2019/lei/l13869.htm', 45),
 ]),
 ('Previdenciária', [
  ('benef',  'Planos de Benefícios da Previdência (Lei 8.213/1991)', 'Lei nº 8.213, de 24 de julho de 1991', B+'leis/l8213cons.htm', 156),
  ('custeio','Custeio da Seguridade Social (Lei 8.212/1991)', 'Lei nº 8.212, de 24 de julho de 1991', B+'leis/l8212cons.htm', 106),
 ]),
 ('Processual', [
  ('jesp',   'Juizados Especiais (Lei 9.099/1995)', 'Lei nº 9.099, de 26 de setembro de 1995', B+'leis/l9099.htm', 97),
  ('acp',    'Ação Civil Pública (Lei 7.347/1985)', 'Lei nº 7.347, de 24 de julho de 1985', B+'leis/L7347Compilada.htm', 22),
  ('ms',     'Mandado de Segurança (Lei 12.016/2009)', 'Lei nº 12.016, de 7 de agosto de 2009', B+'_ato2007-2010/2009/lei/l12016.htm', 29),
  ('arbit',  'Lei de Arbitragem (Lei 9.307/1996)', 'Lei nº 9.307, de 23 de setembro de 1996', B+'leis/l9307.htm', 44),
 ]),
 ('Trabalhista', [
  ('tempor', 'Trabalho Temporário e Terceirização (Lei 6.019/1974)', 'Lei nº 6.019, de 3 de janeiro de 1974', B+'leis/l6019.htm', 20),
  ('domest', 'Empregado Doméstico (LC 150/2015)', 'Lei Complementar nº 150, de 1º de junho de 2015', B+'leis/lcp/lcp150.htm', 47),
 ]),
 ('Tributária', [
  ('lef',    'Execução Fiscal (Lei 6.830/1980)', 'Lei nº 6.830, de 22 de setembro de 1980', B+'leis/l6830.htm', 42),
  ('icms',   'ICMS — Lei Kandir (LC 87/1996)', 'Lei Complementar nº 87, de 13 de setembro de 1996', B+'leis/lcp/lcp87.htm', 36),
  ('iss',    'ISS (LC 116/2003)', 'Lei Complementar nº 116, de 31 de julho de 2003', B+'leis/lcp/lcp116.htm', 10),
 ]),
]

# leis acrescentadas em 27/10/2026 (lista em laws_novas.py): entram nas areas, em ordem alfabetica
import unicodedata as _u
from laws_novas import NOVAS as _NOVAS
_d = {a: list(it) for a, it in LAWS}
for _a, _it in _NOVAS: _d.setdefault(_a, []).extend(_it)
LAWS = sorted(_d.items(), key=lambda x: ''.join(c for c in _u.normalize('NFD', x[0]) if _u.category(c) != 'Mn'))
