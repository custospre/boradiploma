/* GraDireito - Service Worker (PWA)
   Faz o app abrir mesmo sem internet (guarda os arquivos no aparelho)
   e, mais pra frente, vai receber os lembretes de prazo (push).
   Troque a versao do cache sempre que publicar uma atualizacao. */

const CACHE = 'gradireito-v4';

// Arquivos que ficam guardados pra abrir offline (o "esqueleto" do app).
// O app.html (grande, ~12 MB) entra no cache na 1a vez que abrir.
const APP_SHELL = [
  './',
  './app.html',
  './manifest.webmanifest',
  './icons/icon-192.png',
  './icons/icon-512.png'
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE).then((cache) => cache.addAll(APP_SHELL)).catch(() => {})
  );
  self.skipWaiting();
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(keys.filter((k) => k !== CACHE).map((k) => caches.delete(k)))
    )
  );
  self.clients.claim();
});

// Estrategia: tenta a rede; se falhar (sem internet), usa o que esta guardado.
self.addEventListener('fetch', (event) => {
  const req = event.request;
  if (req.method !== 'GET') return;
  event.respondWith(
    fetch(req)
      .then((resp) => {
        const copy = resp.clone();
        caches.open(CACHE).then((cache) => cache.put(req, copy)).catch(() => {});
        return resp;
      })
      .catch(() => caches.match(req).then((hit) => hit || caches.match('./app.html')))
  );
});

// --- Lembretes de prazo (push) --- (sera ativado na Fase 3) ---
self.addEventListener('push', (event) => {
  let data = { title: 'GraDireito', body: 'Voce tem um prazo chegando.' };
  try { if (event.data) data = event.data.json(); } catch (e) {}
  event.waitUntil(
    self.registration.showNotification(data.title || 'GraDireito', {
      body: data.body || '',
      icon: './icons/icon-192.png',
      badge: './icons/icon-192.png',
      data: data.url || './app.html'
    })
  );
});

self.addEventListener('notificationclick', (event) => {
  event.notification.close();
  event.waitUntil(clients.openWindow(event.notification.data || './app.html'));
});
