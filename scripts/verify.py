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
palette = ["#00f0ff","#ffd700","#a855f7","#ff4d6d","#00ff88","#ffffff"]
huella = "".join([f'<div style="background:{palette[int(c,16)%len(palette)]};height:18px;border-radius:3px"></div>' for c in hexa[:64]])
try:
    firma = open("assets/branding/firma-valdovinos.svg").read()
except: firma = "<b style='color:#ffd700;font-size:34px'>Valdovinos</b>"
html = """<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>__FOLIO__</title>
<style>
*{box-sizing:border-box}
body{background:#050810;font-family:system-ui;margin:0;padding:12px}
.cert{background:linear-gradient(160deg,#0b1226,#1a0b2e 50%,#0b1226);color:#fff;width:100%;max-width:680px;margin:auto;border:3px solid #d4af37;border-radius:20px;padding:22px}
.top{text-align:center}
.top small{letter-spacing:3px;color:#ffd700;font-weight:800;font-size:11px}
h1{margin:8px 0 0;font-size:28px} h1 span{color:#00f0ff}
.bar{height:14px;display:flex;border-radius:99px;overflow:hidden;margin:14px 0;border:1px solid #333}
.h{width:51%;background:#00f0ff;color:#000;font-weight:800;text-align:center;font-size:11px;line-height:14px}
.ai{width:49%;background:#a855f7;color:#fff;font-weight:800;text-align:center;font-size:11px;line-height:14px}
h2{color:#ffd700;font-size:20px;text-align:center;border-top:2px solid #d4af37;border-bottom:2px solid #d4af37;padding:12px;word-break:break-all}
.fila{background:rgba(0,0,0,.35);border:1px solid #2a2a4a;border-radius:12px;padding:10px;margin:10px 0}
.etiqueta{color:#ffd700;font-size:11px;letter-spacing:2px;font-weight:800}
.valor{word-break:break-all;font-size:14px;line-height:1.4;margin-top:4px}
.kintsugi{text-align:center;color:#d4af37;letter-spacing:3px;font-size:12px;margin:12px 0}
.sello-wrap{display:flex;justify-content:center;margin:16px 0}
.sello{width:160px;height:160px;border-radius:50%;background:conic-gradient(from 0deg,#00f0ff,#a855f7,#ffd700,#ff4d6d,#00f0ff);display:flex;align-items:center;justify-content:center;animation:girar 7s linear infinite;padding:6px}
@keyframes girar{to{transform:rotate(360deg)}}
.sello-in{width:128px;height:128px;border-radius:50%;background:#050810;color:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;font-size:12px;line-height:1.3;border:2px dashed gold}
.huella{display:grid;grid-template-columns:repeat(8,1fr);gap:3px;margin-top:8px}
.firma-box{text-align:center;background:rgba(0,0,0,.45);border:1px solid #d4af37;border-radius:16px;padding:16px;margin-top:14px}
.firma-box svg{width:300px;max-width:100%;filter:drop-shadow(0 0 10px gold)}
.footer{text-align:center;font-size:12px;color:#9ab;margin-top:14px;line-height:1.4}
@media print{body{background:#fff} .cert{box-shadow:none}}
</style></head><body><div class="cert">
<div class="top"><small>KRONOS2099 • ARKHE-ZERO • TOLUCA-GLOBAL</small><h1>ARKHE<span>-ZERO</span></h1><p>CERTIFICADO DE VERIFICACIÓN DE LEGADO</p><div class="bar"><div class="h">51% HUMANO</div><div class="ai">49% IA</div></div></div>
<h2>__FOLIO__</h2>
<div class="kintsugi">✦ KINTSUGI • GRIETAS DORADAS ✦</div>
<div class="fila"><div class="etiqueta">ARCHIVO</div><div class="valor">__ARCHIVO__</div></div>
<div class="fila"><div class="etiqueta">SHA-256</div><div class="valor">__SHA__</div></div>
<div class="fila"><div class="etiqueta">TAMAÑO • FECHA</div><div class="valor">__TAMANO__ bytes • __FECHA__</div></div>
<div class="fila"><div class="etiqueta">AUTOR • MODELO</div><div class="valor">Valdovinos • 51% Humano / 49% IA</div></div>
<div class="fila"><div class="etiqueta">HUELLA VISUAL OFFLINE • ÚNICA POR HASH • SIN INTERNET</div><div class="huella">__HUELLA__</div><div class="valor" style="font-size:12px;color:#9ab">Cada cuadrito viene de tu SHA-256. Si el archivo cambia una letra, la huella cambia por completo.</div></div>
<div class="sello-wrap"><div class="sello"><div class="sello-in"><b>ARKHE-ZERO</b>VERIFICADO<br>51 / 49<br>SELLO CROMÁTICO</div></div></div>
<div class="firma-box"><div class="etiqueta">FIRMA DEL SOBERANO</div>__FIRMA__<br><small>Autor Humano • Dueño de la visión • Co-firmado 51/49</small></div>
<div class="footer">Verificable en segundos comparando su SHA-256. Si el hash no coincide, el folio ya no es válido. Hasta 2099.</div>
</div></body></html>"""
html = html.replace("__FOLIO__", folio).replace("__SHA__", hexa).replace("__ARCHIVO__", out["archivo"]).replace("__TAMANO__", str(out["tamano"])).replace("__FECHA__", ahora).replace("__FIRMA__", firma).replace("__HUELLA__", huella)
with open(folio+".html","w") as f: f.write(html)
print("FOLIO:", folio)
print("Certificado V3 guardado en:", folio+".html")
