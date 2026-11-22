# IETF 128 Hackathon - KRONOS2099 / ARKHE-ZERO
# Kuala Lumpur, 6-12 Marzo 2027 - Participación remota posible

## Proyecto
Verificador offline de autoría humano-IA, modelo 51/49.

## Qué vamos a codear en el Hackathon
- Buscador público por folio / SHA-256
- Carpeta /verify/ con un HTML estable por folio, como pide RFC 6778
- Exportar certificado en JSON + HTML con misma estructura

## Demo en 2 minutos
1. python3 scripts/verify.py README.md
2. Se genera folio KRONOS-20261121-604A4EF0
3. Se abre certificado V5 Leyenda con sello y firma
4. Cualquiera puede verificar que el hash cuadra, sin subir el archivo

## Autor
Marco Antonio Rojas Valdovinos, Toluca-Global, Mexico
Modelo: 51% Humano decide, 49% IA ordena y construye
Repo: github.com/MarcoValdovinos/KRONOS2099
Draft: draft-valdovinos-arkhe-zero-00

## Cómo participar sin viajar
- Seguir lista de correo y Discussions del repo
- Comentar el draft en GitHub Issues
- Probar el verificador en Termux o en Pages
