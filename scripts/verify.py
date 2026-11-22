#!/usr/bin/env python3
import hashlib, json, sys, os, datetime
ruta = sys.argv[1] if len(sys.argv)>1 else "README.md"
h = hashlib.sha256()
with open(ruta,"rb") as f:
    for chunk in iter(lambda: f.read(8192), b""): h.update(chunk)
hexa = h.hexdigest()
fecha = datetime.datetime.now().strftime("%Y%m%d")
folio = f"KRONOS-{fecha}-{hexa[:8].upper()}"
out = {"folio":folio,"sha256":hexa,"archivo":os.path.basename(ruta),"tamano":os.path.getsize(ruta),"fecha":datetime.datetime.now().isoformat(),"autor":"Valdovinos","modelo":"51% Humano / 49% IA"}
print("FOLIO:", folio)
print("SHA-256:", hexa)
print("ARCHIVO:", out["archivo"])
with open(folio+".json","w") as j: json.dump(out,j,indent=2)
print("Recibo guardado en:", folio+".json")
