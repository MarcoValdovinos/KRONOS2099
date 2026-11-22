#!/usr/bin/env python3
import hashlib, json, sys, os, datetime
ruta = sys.argv[1] if len(sys.argv)>1 else "README.md"
h = hashlib.sha256()
with open(ruta,"rb") as f:
    for chunk in iter(lambda: f.read(8192), b""): h.update(chunk)
hexa = h.hexdigest()
fecha = datetime.datetime.now().strftime("%Y%m%d")
folio = f"KRONOS-{fecha}-{hexa[:8].upper()}"
ahora = datetime.datetime.now().isoformat()
out = {"folio":folio,"sha256":hexa,"archivo":os.path.basename(ruta),"tamano":os.path.getsize(ruta),"fecha":ahora,"autor":"Valdovinos","modelo":"51% Humano / 49% IA"}
with open(folio+".json","w") as j: json.dump(out,j,indent=2)
try:
    firma = open("assets/branding/firma-valdovinos.svg").read()
except: firma = "<b style='color:gold;font-size:32px'>Valdovinos</b>"
html = """<!doctype html><html lang="es"><head><meta charset="utf-8"><title>__FOLIO__</title>
<style>
body{background:#050810;font-family:system-ui;display:flex;justify-content:center;padding:16px;margin:0}
.cert{background:linear-gradient(160deg,#0b1226,#1a0b2e 50%,#0b1226);color:#e8f6ff;width:100%;max-width:720px;border:3px solid #d4af37;border-radius:22px;padding:28px;box-shadow:0 0 40px rgba(212,175,55,.5), inset 0 0 0 2px #111}
.top{text-align:center} .top small{letter-spacing:4px;color:#ffd700;font-weight:800}
h1{margin:6px 0;font-size:32px;color:#fff} h1 span{color:#00f0ff}
.bar{height:14px;display:flex;border-radius:99px;overflow:hidden;margin:12px 0;border:1px solid #333}
.h{width:51%;background:#00f0ff;color:#000;font-weight:800;text-align:center;font-size:11px;line-height:14px}
.ai{width:49%;background:#a855f7;color:#fff;font-weight:800;text-align:center;font-size:11px;line-height:14px}
h2{color:#ffd700;font-size:24px;text-align:center;border-top:2px solid #d4af37;border-bottom:2px solid #d4af37;padding:12px;letter-spacing:1px}
table{width:100%;border-collapse:collapse} td{padding:9px;border-bottom:1px solid #2a2a4a;word-break:break-all} td:first-child{font-weight:800;color:#ffd700;width:120px}
.kintsugi{text-align:center;color:#d4af37;letter-spacing:6px;margin:10px 0}
.sello-wrap{display:flex;justify-content:center;gap:22px;align-items:center;margin:18px 0;flex-wrap:wrap}
.sello{width:160px;height:160px;border-radius:50%;background:conic-gradient(from 0deg,#00f0ff,#a855f7,#ffd700,#ff4d6d,#00f0ff);display:flex;align-items:center;justify-content:center;animation:girar 7s linear infinite;padding:6px;box-shadow:0 0 25px gold}
@keyframes girar{to{transform:rotate(360deg)}}
.sello-in{width:128px;height:128px;border-radius:50%;background:#050810;color:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;font-size:12px;line-height:1.3;border:2px dashed gold}
.qr{background:#fff;padding:8px;border-radius:14px}
.firma-box{text-align:center;background:#00000066;border:1px solid #d4af37;border-radius:16px;padding:14px;margin-top:10px}
.firma-box svg{width:300px;max-width:90%;filter:drop-shadow(0 0 10px gold)}
.footer{text-align:center;font-size:12px;color:#9ab;margin-top:14px}
@media print{body{background:#fff} .cert{box-shadow:none}}
</style></head><body><div class="cert">
<div class="top"><small>KRONOS2099 • ARKHE-ZERO • TOLUCA-GLOBAL</small><h1>ARKHE<span>-ZERO</span></h1><p>CERTIFICADO DE VERIFICACIÓN DE LEGADO</p><div class="bar"><div class="h">51% HUMANO</div><div class="ai">49% IA</div></div></div>
<h2>__FOLIO__</h2>
<div class="kintsugi">✦ ── KINTSUGI • GRIETAS DORADAS ── ✦</div>
<table><tr><td>Archivo</td><td>__ARCHIVO__</td></tr><tr><td>SHA-256</td><td>__SHA__</td></tr><tr><td>Tamaño</td><td>__TAMANO__ bytes</td></tr><tr><td>Fecha</td><td>__FECHA__</td></tr><tr><td>Autor</td><td>Valdovinos</td></tr><tr><td>Modelo</td><td>51% Humano / 49% IA</td></tr></table>
<div class="sello-wrap"><div class="sello"><div class="sello-in"><b>ARKHE-ZERO</b>VERIFICADO<br>51 / 49<br>SELLO CROMÁTICO</div></div>
<img class="qr" src="https://api.qrserver.com/v1/create-qr-code/?size=140x140&data=__FOLIO__|__SHA__"></div>
<div class="firma-box"><small style="color:#ffd700;letter-spacing:3px">FIRMA DEL SOBERANO • VALDOVINOS</small><br>__FIRMA__<br><small>Autor Humano • Dueño de la visión • Cada verificación es co-firmada</small></div>
<div class="footer">Si el archivo cambia una sola letra, el hash cambia y el folio ya no coincide. Verificable en segundos, hasta 2099.</div>
</div></body></html>"""
html = html.replace("__FOLIO__", folio).replace("__SHA__", hexa).replace("__ARCHIVO__", out["archivo"]).replace("__TAMANO__", str(out["tamano"])).replace("__FECHA__", ahora).replace("__FIRMA__", firma)
with open(folio+".html","w") as f: f.write(html)
print("FOLIO:", folio)
print("Certificado V2 guardado en:", folio+".html")
