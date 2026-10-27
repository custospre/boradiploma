# leis novas (27/10/2026): área -> (código, nome curto, descrição oficial, URL do Planalto, nº do último artigo esperado)
B='https://www.planalto.gov.br/ccivil_03/'
NOVAS = [
 ('Administrativa', [
  ('acessoinfo','Acesso à Informação (Lei 12.527/2011)', 'Lei nº 12.527, de 18 de novembro de 2011', B+'_ato2011-2014/2011/lei/l12527.htm', 47),
  ('anticorr', 'Lei Anticorrupção (Lei 12.846/2013)', 'Lei nº 12.846, de 1º de agosto de 2013', B+'_ato2011-2014/2013/lei/l12846.htm', 31),
  ('concess',  'Concessões e Permissões (Lei 8.987/1995)', 'Lei nº 8.987, de 13 de fevereiro de 1995', B+'leis/l8987cons.htm', 47),
  ('ppp',      'Parcerias Público-Privadas (Lei 11.079/2004)', 'Lei nº 11.079, de 30 de dezembro de 2004', B+'_ato2004-2006/2004/lei/l11079.htm', 30),
  ('desapr',   'Desapropriação (Decreto-Lei 3.365/1941)', 'Decreto-Lei nº 3.365, de 21 de junho de 1941', B+'decreto-lei/del3365.htm', 43),
  ('lrf',      'Responsabilidade Fiscal (LC 101/2000)', 'Lei Complementar nº 101, de 4 de maio de 2000', B+'leis/lcp/lcp101.htm', 75),
 ]),
 ('Civil', [
  ('autorais', 'Direitos Autorais (Lei 9.610/1998)', 'Lei nº 9.610, de 19 de fevereiro de 1998', B+'leis/l9610.htm', 115),
  ('alienpar', 'Alienação Parental (Lei 12.318/2010)', 'Lei nº 12.318, de 26 de agosto de 2010', B+'_ato2007-2010/2010/lei/l12318.htm', 11),
  ('paternid', 'Investigação de Paternidade (Lei 8.560/1992)', 'Lei nº 8.560, de 29 de dezembro de 1992', B+'leis/l8560.htm', 10),
  ('libecon',  'Liberdade Econômica (Lei 13.874/2019)', 'Lei nº 13.874, de 20 de setembro de 2019', B+'_ato2019-2022/2019/lei/l13874.htm', 20),
 ]),
 ('Constitucional', [
  ('acpop',    'Ação Popular (Lei 4.717/1965)', 'Lei nº 4.717, de 29 de junho de 1965', B+'leis/l4717.htm', 22),
  ('hdata',    'Habeas Data (Lei 9.507/1997)', 'Lei nº 9.507, de 12 de novembro de 1997', B+'leis/l9507.htm', 22),
  ('minj',     'Mandado de Injunção (Lei 13.300/2016)', 'Lei nº 13.300, de 23 de junho de 2016', B+'_ato2015-2018/2016/lei/l13300.htm', 15),
  ('adi',      'ADI e ADC (Lei 9.868/1999)', 'Lei nº 9.868, de 10 de novembro de 1999', B+'leis/l9868.htm', 30),
  ('adpf',     'ADPF (Lei 9.882/1999)', 'Lei nº 9.882, de 3 de dezembro de 1999', B+'leis/l9882.htm', 14),
 ]),
 ('Digital', [
  ('marcocivil','Marco Civil da Internet (Lei 12.965/2014)', 'Lei nº 12.965, de 23 de abril de 2014', B+'_ato2011-2014/2014/lei/l12965.htm', 32),
  ('lgpd',     'LGPD — Proteção de Dados (Lei 13.709/2018)', 'Lei nº 13.709, de 14 de agosto de 2018', B+'_ato2015-2018/2018/lei/l13709compilado.htm', 65),
 ]),
 ('Empresarial', [
  ('propind',  'Propriedade Industrial (Lei 9.279/1996)', 'Lei nº 9.279, de 14 de maio de 1996', B+'leis/l9279.htm', 244),
 ]),
 ('Penal', [
  ('orcrim',   'Organizações Criminosas (Lei 12.850/2013)', 'Lei nº 12.850, de 2 de agosto de 2013', B+'_ato2011-2014/2013/lei/l12850.htm', 27),
  ('lavagem',  'Lavagem de Dinheiro (Lei 9.613/1998)', 'Lei nº 9.613, de 3 de março de 1998', B+'leis/l9613.htm', 18),
  ('intercep', 'Interceptação Telefônica (Lei 9.296/1996)', 'Lei nº 9.296, de 24 de julho de 1996', B+'leis/l9296.htm', 12),
  ('tortura',  'Lei de Tortura (Lei 9.455/1997)', 'Lei nº 9.455, de 7 de abril de 1997', B+'leis/l9455.htm', 4),
  ('pristemp', 'Prisão Temporária (Lei 7.960/1989)', 'Lei nº 7.960, de 21 de dezembro de 1989', B+'leis/l7960.htm', 3),
  ('racismo',  'Crimes de Racismo (Lei 7.716/1989)', 'Lei nº 7.716, de 5 de janeiro de 1989', B+'leis/l7716.htm', 22),
  ('crimtrib', 'Crimes contra a Ordem Tributária (Lei 8.137/1990)', 'Lei nº 8.137, de 27 de dezembro de 1990', B+'leis/l8137.htm', 23),
 ]),
 ('Previdenciária', [
  ('loas',     'LOAS — Assistência Social (Lei 8.742/1993)', 'Lei nº 8.742, de 7 de dezembro de 1993', B+'leis/l8742.htm', 42),
 ]),
 ('Processual', [
  ('mediacao', 'Lei de Mediação (Lei 13.140/2015)', 'Lei nº 13.140, de 26 de junho de 2015', B+'_ato2015-2018/2015/lei/l13140.htm', 48),
  ('jef',      'Juizados Especiais Federais (Lei 10.259/2001)', 'Lei nº 10.259, de 12 de julho de 2001', B+'leis/leis_2001/l10259.htm', 27),
  ('jefaz',    'Juizados da Fazenda Pública (Lei 12.153/2009)', 'Lei nº 12.153, de 22 de dezembro de 2009', B+'_ato2007-2010/2009/lei/l12153.htm', 28),
  ('gratuid',  'Assistência Judiciária Gratuita (Lei 1.060/1950)', 'Lei nº 1.060, de 5 de fevereiro de 1950', B+'leis/l1060.htm', 19),
 ]),
 ('Trabalhista', [
  ('fgts',     'FGTS (Lei 8.036/1990)', 'Lei nº 8.036, de 11 de maio de 1990', B+'leis/l8036consol.htm', 32),
  ('greve',    'Lei de Greve (Lei 7.783/1989)', 'Lei nº 7.783, de 28 de junho de 1989', B+'leis/l7783.htm', 19),
 ]),
]
