# ICANN aplicado a KRONOS2099

ICANN = quien gestiona nombres de dominio y datos de registro.
RDAP = reemplazo de WHOIS, devuelve JSON estructurado, legible por máquina.
IDN = dominios con caracteres no ASCII: ñ, acentos, árabe, chino, hindi.

## Cómo KRONOS2099 encaja

1. RDAP para certificados:
   - RDAP: consultas un dominio, te devuelve JSON con registrante, fecha, estado
   - KRONOS: consultas un folio, te devuelve JSON con autor, fecha, SHA-256, archivo
   - Misma idea: lookup por identificador, respuesta estructurada

2. IDN para impacto global:
   - Tu proyecto es en español e inglés, para Toluca y para el mundo
   - Si compras dominio propio, va a estar en registro ICANN, consultable por RDAP
   - No expongas correo privado en README, solo en config, como pide privacidad de datos de registro

3. Registration Data Accuracy:
   - ICANN pide datos precisos de registro
   - KRONOS pide datos precisos de autoría: folio, hash, fecha, autor 51/49

## Acción
- Mantener Pages en 【entity-github¦canonical_name=github】.io mientras no tengas dominio propio, ya está limpio y reconocido
- Si compras dominio, verificar su RDAP y no usar dominios .click raros que salen en blocklists
- Presentar KRONOS como RDAP para autoría humano-IA en IETF / ICANN

— Valdovinos • Marco Antonio Rojas Valdovinos • 51% Humano decide, 49% IA ordena
