const CACHE="khanh-dan-ai-v1";
const ASSETS=["/","/static/style.css","/static/app.js","/manifest.json","/static/icon.svg"];
self.addEventListener("install",e=>e.waitUntil(caches.open(CACHE).then(c=>c.addAll(ASSETS))));
self.addEventListener("activate",e=>e.waitUntil(caches.keys().then(keys=>Promise.all(keys.filter(k=>k!==CACHE).map(k=>caches.delete(k))))));
self.addEventListener("fetch",e=>{
  if(e.request.method!=="GET" || new URL(e.request.url).pathname.startsWith("/api/")) return;
  e.respondWith(caches.match(e.request).then(cached=>cached||fetch(e.request)));
});
