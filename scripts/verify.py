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
palette = ["#00f0ff","#ffd700","#a855f7","#ff4d6d","#00ff88","#ffffff","#ff9a00","#00c2ff"]
huella = "".join([f'<div style="background:{palette[int(c,16)%len(palette)]};height:16px;border-radius:2px"></div>' for c in hexa[:64]])
try: firma = open("assets/branding/firma-valdovinos.svg").read()
except: firma = "<b style='color:#ffd700;font-size:34px'>Valdovinos</b>"
html = """<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>__FOLIO__</title>
<style>
*{box-sizing:border-box}
body{background:#030308;font-family:system-ui;margin:0;padding:14px}
.cert{position:relative;overflow:hidden;background:linear-gradient(180deg,#0e0e1a,#111827 60%,#0a0a12);color:#fff;width:100%;max-width:700px;margin:auto;border:2px solid #d4af37;border-radius:24px;padding:28px;box-shadow:0 0 0 3px #000,0 0 50px rgba(212,175,55,.4)}
.watermark{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%) rotate(-12deg);font-size:180px;font-weight:900;color:#fff;opacity:.04;letter-spacing:10px;pointer-events:none}
.ribbon{position:absolute;top:18px;right:-45px;background:#ffd700;color:#000;font-weight:900;font-size:12px;letter-spacing:2px;padding:8px 55px;transform:rotate(45deg);box-shadow:0 4px 12px rgba(0,0,0,.5)}
.top{text-align:center;position:relative}
.top small{letter-spacing:4px;color:#ffd700;font-weight:800;font-size:11px}
h1{margin:8px 0 0;font-size:34px;letter-spacing:2px} h1 span{color:#00f0ff}
.sub{color:#cbd5e1;font-size:13px;margin:6px 0}
.bar{height:14px;display:flex;border-radius:99px;overflow:hidden;margin:14px 0;border:1px solid #333}
.h{width:51%;background:#00f0ff;color:#000;font-weight:800;text-align:center;font-size:11px;line-height:14px}
.ai{width:49%;background:#a855f7;color:#fff;font-weight:800;text-align:center;font-size:11px;line-height:14px}
h2{color:#ffd700;font-size:22px;text-align:center;border-top:1px solid #d4af37;border-bottom:1px solid #d4af37;padding:14px;word-break:break-all;letter-spacing:1px}
.fila{background:rgba(0,0,0,.4);border:1px solid #2a2a4a;border-radius:14px;padding:12px;margin:10px 0;position:relative}
.etiqueta{color:#ffd700;font-size:11px;letter-spacing:2px;font-weight:800}
.valor{word-break:break-all;font-size:14px;line-height:1.5;margin-top:4px}
.huella{display:grid;grid-template-columns:repeat(16,1fr);gap:3px;margin-top:10px}
.kintsugi{text-align:center;color:#d4af37;letter-spacing:3px;font-size:12px;margin:14px 0}
.sello-wrap{display:flex;justify-content:center;margin:18px 0}
.firma-box{text-align:center;background:rgba(0,0,0,.5);border:1px solid #d4af37;border-radius:16px;padding:18px;margin-top:14px;position:relative}
.firma-box svg{width:340px;max-width:100%;filter:drop-shadow(0 0 12px gold)}
.footer{text-align:center;font-size:12px;color:#9ab;margin-top:14px;line-height:1.5}
@media print{body{background:#fff} .cert{box-shadow:none} .ribbon{position:absolute}}
</style></head><body><div class="cert"><div class="watermark">2099</div><div class="ribbon">VERIFICADO</div>
<div class="top"><small>KRONOS2099 • ARKHE-ZERO • TOLUCA-GLOBAL</small><h1>ARKHE<span>-ZERO</span></h1><p class="sub">CERTIFICADO DE VERIFICACIÓN DE LEGADO • CO-CREACIÓN HUMANO-IA</p><div class="bar"><div class="h">51% HUMANO</div><div class="ai">49% IA</div></div></div>
<h2>__FOLIO__</h2>
<div class="kintsugi">✦ KINTSUGI • GRIETAS DORADAS • LO ROTO SE VUELVE ORO ✦</div>
<div class="fila"><div class="etiqueta">ARCHIVO VERIFICADO</div><div class="valor">__ARCHIVO__</div></div>
<div class="fila"><div class="etiqueta">SHA-256 • HUELLA CRIPTOGRÁFICA</div><div class="valor">__SHA__</div></div>
<div class="fila"><div class="etiqueta">TAMAÑO • FECHA • AUTOR</div><div class="valor">__TAMANO__ bytes • __FECHA__ • Valdovinos • 51% Humano / 49% IA</div></div>
<div class="fila"><div class="etiqueta">HUELLA VISUAL OFFLINE • ÚNICA POR HASH • SIN INTERNET</div><div class="huella">__HUELLA__</div><div class="valor" style="font-size:12px;color:#9ab">Cada cuadrito viene de tu SHA-256. Si cambias una letra del archivo, la huella cambia por completo.</div></div>
<div class="sello-wrap[STRIPPED 16 bytes]0 0 200 200" width="175" height="175"><defs><path id="circ" d="M100,100 m -72,0 a72,72 0 1,1 144,0 a72,72 0 1,1 -144,0"/><linearGradient id="gg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#00f0ff"/><stop offset="0.5" stop-color="#ffd700"/><stop offset="1" stop-color="#a855f7"/></linearGradient></defs><circle cx="100" cy="100" r="98" fill="url(#gg)"/><circle cx="100" cy="100" r="80" fill="#050810"/><text font-size="12.5" fill="#ffd700" letter-spacing="2"><textPath href="#circ">ARKHE-ZERO • VERIFICADO • 51% HUMANO 49% IA • KRONOS2099 •</textPath></text><text x="100" y="100" text-anchor="middle" fill="#fff" font-size="22" font-weight="900">ARKHE</text><text x="100" y="122" text-anchor="middle" fill="#00f0ff" font-size="15" font-weight="800">ZERO</text><text x="100" y="140" text-anchor="middle" fill="#ffd700" font-size="10">SELLO CROMÁTICO</text></svg></div>
<div class="firma-box"><div class="etiqueta">FIRMA DEL SOBERANO • VALDOVINOS</div>__FIRMA__<br><small>Autor Humano • Dueño de la visión • Cada verificación es co-firmada 51/49</small></div>
<div class="footer">Verificable en segundos comparando su SHA-256. Si el hash no coincide, el folio ya no es válido. • kronos2099.com • Hasta 2099</div>
</div></body></html>"""
html = html.replace("__FOLIO__", folio).replace("__SHA__", hexa).replace("__ARCHIVO__", out["archivo"]).replace("__TAMANO__", str(out["tamano"])).replace("__FECHA__", ahora).replace("__FIRMA__", firma).replace("__HUELLA__", huella)
with open(folio+".html","w") as f: f.write(html)
print("FOLIO:", folio)
print("Certificado V4 Dios guardado en:", folio+".html")
