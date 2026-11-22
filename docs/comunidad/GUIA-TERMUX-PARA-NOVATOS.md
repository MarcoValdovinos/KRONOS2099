# Guía Termux + GitHub para novatos, por Valdovinos
## Sin esperar nada a cambio

Yo empecé desde cero en Termux, en mi celular, sin computadora. Me atoré con todo: con el .git en home, con el origin not found, con el JSON feo. Esto es lo que me hubiera gustado que alguien me dijera.

### 1. No hagas git init en tu home ~
Si haces `git init` en `~`, te va a querer subir todo tu celular. Hazlo solo dentro de tu carpeta:
`mkdir -p ~/KRONOS2099 && cd ~/KRONOS2099 && git init`

### 2. Si tu origin está mal, no borres nada
Solo corrígelo:
`git remote remove origin`
`git remote add origin https://github.com/TU_USUARIO/TU_REPO.git`
`git push -u origin main`

### 3. Si GitHub te dice Repository not found
Es porque el repo todavía no existe en GitHub. Créalo con:
`gh repo create TU_REPO --public --source=. --remote=origin --push`

### 4. Si tu carpeta no se ve en GitHub
Git no guarda carpetas vacías. Ponle un .gitkeep:
`find . -type d -empty -not -path "./.git*" -exec touch {}/.gitkeep \;`

### 5. Verifica sin subir tu archivo
Usa `scripts/verify.py` o `apps/web-verify/`. Todo se calcula en tu celular.

Si estás atorado, abre un Issue en este repo. Yo o alguien de la comunidad te ayudamos, sin esperar nada a cambio. Todos empezamos desde cero.

— Valdovinos • KRONOS2099 • ARKHE-ZERO • 51% Humano / 49% IA
