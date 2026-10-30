/* BoraDiploma Escola mudou para https://escola.boradiploma.com.br
   Este service worker so limpa a copia antiga e se desliga. */
self.addEventListener('install', function () { self.skipWaiting(); });
self.addEventListener('activate', function (event) {
  event.waitUntil(
    caches.keys().then(function (keys) {
      return Promise.all(keys.filter(function (k) { return k.indexOf('bdescola-') === 0; }).map(function (k) { return caches.delete(k); }));
    }).then(function () { return self.registration.unregister(); })
  );
});
