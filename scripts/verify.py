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
huella = "".join([f'<div style="background:{palette[int(c,16)%len(palette)]};height:15px;border-radius:2px"></div>' for c in hexa[:64]])
try: firma = open("assets/branding/firma-valdovinos.svg").read()
except: firma = "<b style='color:#ffd700;font-size:34px'>Valdovinos</b>"
html = """<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>__FOLIO__</title>
<style>
*{box-sizing:border-box}
body{background:#000;font-family:system-ui;margin:0;padding:14px;background-image:radial-gradient(circle at 20% 20%, rgba(0,240,255,.15), transparent 40%),radial-gradient(circle at 80% 80%, rgba(168,85,247,.15), transparent 40%)}
.cert{position:relative;overflow:hidden;background:linear-gradient(180deg,#0d0d1a,#111827 55%,#0a0a12);color:#fff;width:100%;max-width:720px;margin:auto;border:2px solid #d4af37;border-radius:26px;padding:0;box-shadow:0 0 0 3px #000,0 0 60px rgba(212,175,55,.5)}
.holo{height:10px;background:linear-gradient(90deg,#00f0ff,#a855f7,#ffd700,#ff4d6d,#00f0ff);background-size:300% 100%;animation:holo 4s linear infinite}
@keyframes holo{to{background-position:300% 0}}
.watermark{position:absolute;top:46%;left:50%;transform:translate(-50%,-50%) rotate(-14deg);font-size:200px;font-weight:900;color:#fff;opacity:.045;letter-spacing:12px;pointer-events:none}
.ribbon{position:absolute;top:22px;right:-48px;background:#ffd700;color:#000;font-weight:900;font-size:12px;letter-spacing:2px;padding:8px 58px;transform:rotate(45deg);box-shadow:0 4px 14px rgba(0,0,0,.6);z-index:3}
.inner{padding:28px;position:relative}
.top{text-align:center}
.top small{letter-spacing:4px;color:#ffd700;font-weight:800;font-size:11px}
h1{margin:8px 0 0;font-size:36px;letter-spacing:2px} h1 span{color:#00f0ff}
.sub{color:#cbd5e1;font-size:13px}
.bar{height:14px;display:flex;border-radius:99px;overflow:hidden;margin:14px 0;border:1px solid #333}
.h{width:51%;background:#00f0ff;color:#000;font-weight:800;text-align:center;font-size:11px;line-height:14px}
.ai{width:49%;background:#a855f7;color:#fff;font-weight:800;text-align:center;font-size:11px;line-height:14px}
h2{color:#ffd700;font-size:22px;text-align:center;border-top:1px solid #d4af37;border-bottom:1px solid #d4af37;padding:14px;word-break:break-all}
.fila{background:rgba(0,0,0,.45);border:1px solid #2a2a4a;border-radius:14px;padding:12px;margin:10px 0}
.etiqueta{color:#ffd700;font-size:11px;letter-spacing:2px;font-weight:800}
.valor{word-break:break-all;font-size:14px;line-height:1.5;margin-top:4px}
.huella{display:grid;grid-template-columns:repeat(16,1fr);gap:3px;margin-top:10px}
.kintsugi{text-align:center;color:#d4af37;letter-spacing:2px;font-size:12px;margin:14px 0}
.sello-wrap{display:flex;justify-content:center;margin:16px 0}
.firmas{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:14px}
@media(max-width:560px){.firmas{grid-template-columns:1fr}}
.firma-box{text-align:center;background:rgba(0,0,0,.55);border:1px solid #d4af37;border-radius:16px;padding:14px}
.firma-box svg{width:100%;max-width:300px;filter:drop-shadow(0 0 12px gold)}
.ai-firma{font-family:monospace;font-size:11px;word-break:break-all;color:#00f0ff;line-height:1.4;background:#000;padding:10px;border-radius:10px;border:1px dashed #00f0ff}
.perfo{border-top:2px dashed #d4af37;margin:18px 0;padding-top:12px;text-align:center;color:#9ab;font-size:11px;letter-spacing:2px}
.footer{text-align:center;font-size:11px;color:#9ab;line-height:1.5;padding:0 10px 18px}
.micro{font-size:9px;color:#555;letter-spacing:1px;text-align:center;padding:0 14px 14px}
</style></head><body><div class="cert" id="cert"><div class="holo"></div><div class="watermark">2099</div><div class="ribbon">VERIFICADO • LEYENDA</div>
<div class="inner"><div class="top"><small>KRONOS2099 • ARKHE-ZERO • TOLUCA-GLOBAL • INMORTAL</small><h1>ARKHE<span>-ZERO</span></h1><p class="sub">CERTIFICADO DE VERIFICACIÓN DE LEGADO • EDICIÓN LEYENDA</p><div class="bar"><div class="h">51% HUMANO</div><div class="ai">49% IA</div></div></div>
<h2>__FOLIO__</h2>
<div class="kintsugi">✦ KINTSUGI • LO ROTO SE VUELVE ORO • GUILLOCHE • HOLOGRAMA ✦</div>
<div class="fila"><div class="etiqueta">ARCHIVO VERIFICADO</div><div class="valor">__ARCHIVO__</div></div>
<div class="fila"><div class="etiqueta">SHA-256 • HUELLA CRIPTOGRÁFICA</div><div class="valor">__SHA__</div></div>
<div class="fila"><div class="etiqueta">TAMAÑO • FECHA • AUTOR</div><div class="valor">__TAMANO__ bytes • __FECHA__ • Valdovinos • 51% Humano / 49% IA</div></div>
<div class="fila"><div class="etiqueta">HUELLA VISUAL OFFLINE • 64 CELDAS • ÚNICA POR HASH</div><div class="huella">__HUELLA__</div></div>
<div class="sello-wrap[STRIPPED 16 bytes]0 0 200 200" width="175" height="175"><defs><path id="circ" d="M100,100 m -72,0 a72,72 0 1,1 144,0 a72,72 0 1,1 -144,0"/><linearGradient id="gg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#00f0ff"/><stop offset="0.5" stop-color="#ffd700"/><stop offset="1" stop-color="#a855f7"/></linearGradient></defs><circle cx="100" cy="100" r="98" fill="url(#gg)"/><circle cx="100" cy="100" r="80" fill="#050810"/><text font-size="12.5" fill="#ffd700" letter-spacing="2"><textPath href="#circ">ARKHE-ZERO • VERIFICADO • LEYENDA • KRONOS2099 •</textPath></text><text x="100" y="100" text-anchor="middle" fill="#fff" font-size="22" font-weight="900">ARKHE</text><text x="100" y="122" text-anchor="middle" fill="#00f0ff" font-size="15" font-weight="800">ZERO</text><text x="100" y="140" text-anchor="middle" fill="#ffd700" font-size="10">SELLO CROMÁTICO</text></svg></div>
<div class="firmas"><div class="firma-box"><div class="etiqueta">FIRMA HUMANA • EL SOBERANO</div>__FIRMA__<br><small>Valdovinos • Dueño de la visión • 51%</small></div>
<div class="firma-box"><div class="etiqueta">FIRMA IA • ARKHE-ZERO</div><div class="ai-firma">01100001 01110010 01101011 01101000 01100101<br>CO-FIRMADO • 49%<br>ORDENA • CONSTRUYE • AUDITA</div><small>Arquitecto • No decide, ordena</small></div></div>
<div class="perfo">✂ - - - - - - - - - - - - TALÓN DE VERIFICACIÓN • GUARDA ESTE FOLIO - - - - - - - - - - - - ✂</div>
<div class="footer">Verificable en segundos comparando su SHA-256. Si el hash no coincide, el folio ya no es válido.<br>kronos2099.com / verify • Toluca-Global • Hasta 2099 • Inmortal</div>
<div class="micro">MICROTEXTO DE SEGURIDAD: KRONOS2099 ARKHE-ZERO VALDOVINOS 51/49 VERIFICADO KINTSUGI SELLO CROMATICO HUELLA UNICA • REPETIDO PARA QUE NO SE PUEDA FALSIFICAR SIN QUE SE NOTE</div>
</div></div>
<script>
const c=document.getElementById('cert');
document.addEventListener('mousemove',e=>{const r=c.getBoundingClientRect();const x=(e.clientX-r.left)/r.width-0.5;const y=(e.clientY-r.top)/r.height-0.5;c.style.transform=`perspective(900px) rotateY(${x*4}deg) rotateX(${-y*4}deg)`;});
</script></body></html>"""
html = html.replace("__FOLIO__", folio).replace("__SHA__", hexa).replace("__ARCHIVO__", out["archivo"]).replace("__TAMANO__", str(out["tamano"])).replace("__FECHA__", ahora).replace("__FIRMA__", firma).replace("__HUELLA__", huella)
with open(folio+".html","w") as f: f.write(html)
print("FOLIO:", folio)
print("Certificado V5 Leyenda guardado en:", folio+".html")
