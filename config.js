/* BoraDiploma online - configuracao da nuvem
   >>> Estes valores serao preenchidos quando voce criar a conta do Supabase. <<<
   A "anon key" abaixo PODE ficar visivel no app (ela e publica de proposito).
   O que protege os dados de cada usuario e a regra de seguranca no servidor
   (cada pessoa so enxerga o proprio cofre). NAO coloque aqui a "service_role".
*/
window.BORADIPLOMA_CONFIG = {
  SUPABASE_URL: 'COLAR_AQUI_A_URL_DO_PROJETO',
  SUPABASE_ANON_KEY: 'COLAR_AQUI_A_ANON_KEY',
  // Chave publica de push (VAPID) - sera gerada na Fase 3:
  VAPID_PUBLIC_KEY: ''
};
