# 2a leva (27/10/2026). destino: 'codigos' | 'estatutos' | nome da área da Legislação Complementar
B='https://www.planalto.gov.br/ccivil_03/'
NOVAS2 = [
 ('codigos', [
  ('cpm',      'Código Penal Militar', 'Decreto-Lei nº 1.001, de 21 de outubro de 1969 — Código Penal Militar', B+'decreto-lei/del1001.htm', 410),
  ('cppm',     'Código de Processo Penal Militar', 'Decreto-Lei nº 1.002, de 21 de outubro de 1969 — Código de Processo Penal Militar', B+'decreto-lei/del1002.htm', 718),
  ('cba',      'Código Brasileiro de Aeronáutica', 'Lei nº 7.565, de 19 de dezembro de 1986 — Código Brasileiro de Aeronáutica', B+'leis/l7565compilado.htm', 324),
 ]),
 ('estatutos', [
  ('terra',    'Estatuto da Terra', 'Lei nº 4.504, de 30 de novembro de 1964 — Estatuto da Terra', B+'leis/l4504.htm', 128),
  ('indio',    'Estatuto do Índio', 'Lei nº 6.001, de 19 de dezembro de 1973 — Estatuto do Índio', B+'leis/l6001.htm', 68),
  ('militares','Estatuto dos Militares', 'Lei nº 6.880, de 9 de dezembro de 1980 — Estatuto dos Militares', B+'leis/l6880.htm', 160),
  ('refugiados','Estatuto dos Refugiados', 'Lei nº 9.474, de 22 de julho de 1997 — Estatuto dos Refugiados', B+'leis/l9474.htm', 49),
  ('esporte',  'Lei Geral do Esporte (antigo Estatuto do Torcedor)', 'Lei nº 14.597, de 14 de junho de 2023 — Lei Geral do Esporte', B+'_ato2023-2026/2023/lei/l14597.htm', 217),
 ]),
 ('Administrativa', [
  ('prefeitos','Responsabilidade de Prefeitos (Decreto-Lei 201/1967)', 'Decreto-Lei nº 201, de 27 de fevereiro de 1967', B+'decreto-lei/del0201.htm', 9),
 ]),
 ('Ambiental', [
  ('snuc',     'Unidades de Conservação — SNUC (Lei 9.985/2000)', 'Lei nº 9.985, de 18 de julho de 2000', B+'leis/l9985.htm', 60),
  ('residuos', 'Resíduos Sólidos (Lei 12.305/2010)', 'Lei nº 12.305, de 2 de agosto de 2010', B+'_ato2007-2010/2010/lei/l12305.htm', 57),
  ('hidricos', 'Recursos Hídricos (Lei 9.433/1997)', 'Lei nº 9.433, de 8 de janeiro de 1997', B+'leis/l9433.htm', 57),
 ]),
 ('Civil', [
  ('alienfid', 'Alienação Fiduciária (Decreto-Lei 911/1969)', 'Decreto-Lei nº 911, de 1º de outubro de 1969', B+'decreto-lei/1965-1988/del0911compilado.htm', 8),
  ('incorp',   'Condomínio e Incorporações (Lei 4.591/1964)', 'Lei nº 4.591, de 16 de dezembro de 1964', B+'leis/l4591.htm', 70),
  ('parcel',   'Parcelamento do Solo Urbano (Lei 6.766/1979)', 'Lei nº 6.766, de 19 de dezembro de 1979', B+'leis/l6766.htm', 55),
  ('divorcio', 'Lei do Divórcio (Lei 6.515/1977)', 'Lei nº 6.515, de 26 de dezembro de 1977', B+'leis/l6515.htm', 54),
 ]),
 ('Constitucional', [
  ('crimresp', 'Crimes de Responsabilidade (Lei 1.079/1950)', 'Lei nº 1.079, de 10 de abril de 1950', B+'leis/l1079.htm', 82),
 ]),
 ('Internacional', [
  ('sanjose',  'Pacto de San José da Costa Rica (Decreto 678/1992)', 'Decreto nº 678, de 6 de novembro de 1992 — Convenção Americana sobre Direitos Humanos', B+'decreto/d0678.htm', 82),
  ('convpcd',  'Convenção sobre os Direitos das Pessoas com Deficiência (Decreto 6.949/2009)', 'Decreto nº 6.949, de 25 de agosto de 2009 — Convenção de Nova York', B+'_ato2007-2010/2009/decreto/d6949.htm', 50),
 ]),
 ('Organização Judiciária', [
  ('loman',    'LOMAN — Magistratura Nacional (LC 35/1979)', 'Lei Complementar nº 35, de 14 de março de 1979', B+'leis/lcp/lcp35.htm', 147),
  ('lonmp',    'Lei Orgânica do Ministério Público (Lei 8.625/1993)', 'Lei nº 8.625, de 12 de fevereiro de 1993', B+'leis/l8625.htm', 84),
  ('defens',   'Defensoria Pública (LC 80/1994)', 'Lei Complementar nº 80, de 12 de janeiro de 1994', B+'leis/lcp/lcp80.htm', 148),
 ]),
 ('Penal', [
  ('sistfin',  'Crimes contra o Sistema Financeiro (Lei 7.492/1986)', 'Lei nº 7.492, de 16 de junho de 1986', B+'leis/l7492.htm', 35),
  ('identcrim','Identificação Criminal (Lei 12.037/2009)', 'Lei nº 12.037, de 1º de outubro de 2009', B+'_ato2007-2010/2009/lei/l12037.htm', 9),
  ('protest',  'Proteção a Vítimas e Testemunhas (Lei 9.807/1999)', 'Lei nº 9.807, de 13 de julho de 1999', B+'leis/l9807.htm', 21),
  ('henryborel','Lei Henry Borel (Lei 14.344/2022)', 'Lei nº 14.344, de 24 de maio de 2022', B+'_ato2019-2022/2022/lei/l14344.htm', 34),
 ]),
 ('Saúde', [
  ('sus',      'Lei Orgânica da Saúde — SUS (Lei 8.080/1990)', 'Lei nº 8.080, de 19 de setembro de 1990', B+'leis/l8080.htm', 55),
 ]),
 ('Trabalhista', [
  ('estagio',  'Lei do Estágio (Lei 11.788/2008)', 'Lei nº 11.788, de 25 de setembro de 2008', B+'_ato2007-2010/2008/lei/l11788.htm', 22),
  ('segdesemp','Seguro-Desemprego (Lei 7.998/1990)', 'Lei nº 7.998, de 11 de janeiro de 1990', B+'leis/l7998.htm', 31),
 ]),
 ('Tributária', [
  ('lc214',    'Reforma Tributária — IBS, CBS e IS (LC 214/2025)', 'Lei Complementar nº 214, de 16 de janeiro de 2025', B+'leis/lcp/lcp214.htm', 544),
 ]),
]
