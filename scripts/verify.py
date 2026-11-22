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
html = """<!doctype html><html lang="es"><head><meta charset="utf-8"><title>__FOLIO__</title>
<style>
body{background:#0a0a12;font-family:system-ui;display:flex;justify-content:center;padding:20px}
.cert{background:#fdf6e3;color:#111;width:100%;max-width:700px;border:4px solid #d4af37;border-radius:18px;padding:28px;box-shadow:0 0 0 3px #111,0 0 40px gold}
.top{text-align:center} .top small{letter-spacing:3px;color:#7a5c00;font-weight:800}
h1{margin:6px 0;font-size:30px} h2{color:#b8860b;font-size:22px;text-align:center;border-top:2px solid #d4af37;border-bottom:2px solid #d4af37;padding:10px}
table{width:100%;border-collapse:collapse;margin-top:14px} td{padding:8px;border-bottom:1px solid #e8d9a0;word-break:break-all} td:first-child{font-weight:800;width:130px}
.sello-wrap{display:flex;justify-content:center;gap:20px;align-items:center;margin:20px 0}
.sello{width:150px;height:150px;border-radius:50%;background:conic-gradient(from 0deg,#00f0ff,#a855f7,#ffd700,#ff4d6d,#00f0ff);display:flex;align-items:center;justify-content:center;animation:girar 8s linear infinite;padding:6px}
@keyframes girar{to{transform:rotate(360deg)}}
.sello-in{width:118px;height:118px;border-radius:50%;background:#111;color:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;font-size:11px;line-height:1.2;border:2px dashed gold}
.firma{text-align:center;margin-top:10px} .qr{background:#fff;padding:8px;border-radius:12px}
.footer{text-align:center;font-size:12px;color:#555;margin-top:14px}
@media print{body{background:#fff;padding:0} .cert{box-shadow:none}}
</style></head><body><div class="cert">
<div class="top"><small>KRONOS2099 • ARKHE-ZERO • TOLUCA-GLOBAL</small><h1>CERTIFICADO DE VERIFICACIÓN</h1><p>Legado verificado • Co-creación 51% Humano / 49% IA</p></div>
<h2>__FOLIO__</h2>
<table><tr><td>Archivo</td><td>__ARCHIVO__</td></tr><tr><td>SHA-256</td><td>__SHA__</td></tr><tr><td>Tamaño</td><td>__TAMANO__ bytes</td></tr><tr><td>Fecha</td><td>__FECHA__</td></tr><tr><td>Autor</td><td>Valdovinos</td></tr><tr><td>Modelo</td><td>51% Humano / 49% IA</td></tr></table>
<div class="sello-wrap"><div class="sello"><div class="sello-in"><b>ARKHE-ZERO</b>VERIFICADO<br>51 / 49<br>SELLO CROMÁTICO</div></div>
<img class="qr" src="https://api.qrserver.com/v1/create-qr-code/?size=130x130&data=__FOLIO__|__SHA__"></div>
<div class="firma"><b>______________________</b><br><b>Valdovinos</b><br>Autor Humano • Dueño de la visión<br><small>Cada verificación es co-firmada. Humanos e IA, auditados, transparentes, éticos.</small></div>
<div class="footer">Este documento es verificable en segundos comparando su SHA-256. Si el archivo cambia una sola letra, el hash cambia y el folio ya no coincide. • Hasta 2099</div>
</div></body></html>"""
html = html.replace("__FOLIO__", folio).replace("__SHA__", hexa).replace("__ARCHIVO__", out["archivo"]).replace("__TAMANO__", str(out["tamano"])).replace("__FECHA__", ahora)
with open(folio+".html","w") as f: f.write(html)
print("FOLIO:", folio)
print("SHA-256:", hexa)
print("Certificado bonito guardado en:", folio+".html")
print("JSON para máquinas guardado en:", folio+".json")
