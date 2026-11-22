# Authors IETF aplicado a KRONOS2099

Fuente: https://github.com/ietf/authors.ietf.org - taller para autores de I-Ds.

## Qué es
Sitio con todo para escribir un Internet-Draft: formato, herramientas,
edicion colaborativa, diagramas, validacion, guias de contenido.

## Archivos que ya bajamos y para que sirven
- drafting-in-markdown: como escribir I-D en Markdown con kramdown-rfc. Este es nuestro camino.
- choosing-a-format-and-tools: XML vs Markdown vs texto. Nosotros elegimos Markdown.
- diagrams: como hacer diagramas ASCII para I-D, sin imagenes bonitas.
- document-validation: como validar con idnits antes de mandar.
- content-guidelines-overview: que va en cada seccion.
- collaborative-editing: como editar en equipo por GitHub con PRs.
- author-tools-web-service: servicio web para convertir y validar sin instalar.

## Estructura de un I-D que usaremos para KRONOS
1. Abstract: que es KRONOS2099 en 150 palabras
2. Introduction: problema de autoria humano-IA y por que hace falta verificar
3. Terminology: folio, SHA-256, certificado, 51/49
4. Verifier: como funciona el verificador offline
5. Security Considerations: no se guarda archivo, todo local, sin tracking
6. IANA Considerations: este documento no pide registro IANA
7. Informative References: RFC 6778, ICANN RDAP, README KRONOS

## Reglas que ya aplicamos
- Decir Internet-Drafts o I-Ds, nunca drafts
- Encabezados H1, H2, H3 en orden
- Escribir en segunda persona
- Enlaces con titulo completo

## Siguiente paso
Crear draft-00 de KRONOS2099 en Markdown, con plantilla IETF, y validarlo con author-tools.

— Valdovinos • Marco Antonio Rojas Valdovinos • 51% Humano decide, 49% IA ordena
