# RFC 6778 aplicado a KRONOS2099 / ARKHE-ZERO

RFC 6778 es Informational, no es estándar, pero es consenso del IETF sobre cómo archivar para que no se pierda.

## Mapeo

| Requisito RFC 6778 | Cómo lo cumple KRONOS2099 |
| URI estable por mensaje | Cada folio KRONOS tiene URL estable: /verify/<FOLIO> |
| Buscar por autor, fecha, asunto, ID | Buscar por autor Valdovinos, fecha, nombre de archivo, SHA-256, folio |
| Exportar en formato estándar | Exportar JSON + HTML del certificado, siempre misma estructura |
| Redundancia geográfica | 【entity-GitHub¦canonical_name=GitHub】 Pages + Zenodo DOI + copia local en Termux |
| Integridad del archivo | SHA-256. Si cambia un byte, el folio se invalida |
| No requerir login para archivos abiertos | Verificador público, sin cuenta, offline |

## Lo que nos falta para ser estándar

- Buscador público por folio/hash en la web
- Carpeta /verify/ con un HTML por folio
- Publicar este mapeo como Internet-Draft: draft-valdovinos-arkhe-zero-00

— Valdovinos • 51% Humano decide, 49% IA ordena • Toluca-Global
