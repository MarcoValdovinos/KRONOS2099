# Automated Network Management aplicado a KRONOS2099

IETF: redes tan grandes que ya no se pueden configurar a mano. Se usa YANG para modelar, NETCONF / RESTCONF para configurar, y ANIMA para que la red se auto-configure, se auto-cure y se auto-proteja. RFC 7575, 7576, 8993.

## Cómo KRONOS2099 encaja

- YANG = molde de configuración. KRONOS JSON = molde de verificación: folio, SHA-256, archivo, tamaño, fecha, autor, modelo 51/49
- NETCONF / RESTCONF = mandan configuración. KRONOS = verifica que esa configuración no fue alterada
- ANIMA Self-Protection = si el hash no cuadra, la configuración se rechaza, la red se protege sola

## Ejemplo

Archivo: config-router-toluca.json
- python3 scripts/verify.py config-router-toluca.json
- Folio KRONOS-20261122-XXXX
- Si cambian una línea, SHA-256 cambia, folio inválido, no se aplica

## Para el estándar

KRONOS2099 se presenta como verificación ligera para configuración de red y para autoría humano-IA, compatible con principios de ANIMA.

— Valdovinos • 51% Humano decide, 49% IA ordena • Toluca-Global
