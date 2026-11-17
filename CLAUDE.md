# CLAUDE.md — awesome-catalunya

## Propósito

Selección de software open source que da **soporte específico a Catalunya** — su gobierno autonómico (Generalitat de Catalunya), ayuntamientos, diputaciones, universidades, empresas, infraestructuras y patrimonio. Todo el contenido en español. El foco es Catalunya: el software debe dirigirse específicamente a esta comunidad autónoma o a sus municipios.

## Ámbito

- **4 provincias**: Barcelona, Girona, Lleida, Tarragona.
- Principales ciudades: Barcelona (capital), L'Hospitalet de Llobregat, Terrassa, Badalona, Sabadell, Lleida, Tarragona, Mataró, Santa Coloma de Gramenet, Reus, Girona, Sant Cugat del Vallès, Cornellà de Llobregat, Sant Boi de Llobregat, Manresa, Rubí, Vilanova i la Geltrú, Viladecans, El Prat de Llobregat, Castelldefels, Granollers, Cerdanyola del Vallès, Mollet del Vallès, Gavà, Figueres, Sant Feliu de Llobregat, Vic, Igualada, Vilafranca del Penedès, Tortosa, Olot, Berga, Solsona, Tremp, La Seu d'Urgell, Puigcerdà, Vielha e Mijaran.
- **Universidades**: UB (Universitat de Barcelona), UAB (Universitat Autònoma de Barcelona), UPC (Universitat Politècnica de Catalunya), UPF (Universitat Pompeu Fabra), URV (Universitat Rovira i Virgili), UdG (Universitat de Girona), UdL (Universitat de Lleida), URL (Universitat Ramon Llull), UOC (Universitat Oberta de Catalunya), UVic-UCC (Universitat de Vic).
- **Instituciones**: Gencat (Generalitat de Catalunya), AOC (Consorci Administració Oberta de Catalunya), ICGC (Institut Cartogràfic i Geològic de Catalunya), Idescat (Institut d'Estadística de Catalunya), CatSalut (Servei Català de la Salut), XTEC (Xarxa Telemàtica Educativa de Catalunya), CTTI (Centre de Telecomunicacions i Tecnologies de la Informació), Diputació de Barcelona, Ajuntament de Barcelona, BSC (Barcelona Supercomputing Center), Projecte AINA, Softcatalà.

## Criterios de inclusión

### Incluir

- Software que interactúa con la **Generalitat de Catalunya** o sus organismos (Gencat, AOC, CTTI, Sede Electrónica).
- Herramientas para **ayuntamientos** de Catalunya (Ajuntament de Barcelona, diputaciones).
- Software de **universidades catalanas** (UB, UAB, UPC, UPF, URV, UdG, UdL, URL, UOC) cuando sea específico de la región o la universidad.
- Herramientas de **datos abiertos** de Catalunya (dadesobertes.gencat.cat, Open Data BCN, Idescat).
- Software relacionado con el **ICGC** (cartografía, geología, territorio).
- Herramientas de **educación** catalanas (XTEC, Departament d'Educació, Selectivitat).
- Software de **transporte** catalán (FGC, Rodalies de Catalunya, TMB, ATM).
- Software de **lengua catalana** (NLP, traducción, diccionarios, Softcatalà, Projecte AINA).
- Herramientas de **salud** (CatSalut, hospitales catalanes).
- Software de **smart cities** para ciudades catalanas (Sentilo, Barcelona Digital City).
- Proyectos de **participación ciudadana** (Decidim, participa.gencat.cat).
- Software sobre **transparencia y contratación pública** catalana.
- Herramientas de **cartografía y SIG** específicas de Catalunya.

### No incluir

- Software **genérico** que funciona en toda España sin funcionalidad específica de Catalunya — eso pertenece a awesome-spain.
- Software de **ámbito europeo** — eso pertenece a awesome-europe.
- Software de **otras comunidades autónomas** españolas.
- Software creado por catalanes que **no tiene funcionalidad específica** de la región.
- Repositorios **archivados o de solo lectura**. Si uno ya está en la lista, se decide con «Permanencia».
- Repos donde el autor indica que el proyecto está **roto, sin mantenimiento o deprecado**.
- Repos **sin README significativo** o que son claramente repos de test/experimento.
- Ejercicios de clase o trabajos académicos sin utilidad real.

### Zona gris — usar criterio

- Proyectos de universidades catalanas que podrían ser genéricos — incluir si tienen datos o configuración específica de Catalunya.
- Software que cubre Catalunya junto con otras regiones — incluir si Catalunya es un foco principal.
- Herramientas de lengua catalana: incluir si son específicas del catalán, no si son herramientas NLP genéricas.

## Estándares de calidad

**Mismo listón que [awesome-spain](https://github.com/GeiserX/awesome-spain):**

- **No repos archivados**: si una entrada resulta estar archivada, se propone retirarla y pasa a `DELETED.md` cuando Sergio lo aprueba (ver «Permanencia»).
- **Nada viejo sin comprobar**: lo viejo sin reputación se queda solo si se comprueba que funciona y ninguna entrada mantenida de la lista hace lo mismo (ver «Permanencia»).
- **No repos rotos**: si el README dice «deprecated», «broken», «no longer maintained», «use X instead» o similar, no se incluye. Si ya está listado, se decide con «Permanencia»: «use X instead» con X mantenido en la lista cuenta como sustituido, y «no longer maintained» por sí solo no retira una entrada con reputación que sigue funcionando.
- **Estrellas mínimas**: 5 estrellas y 3 meses de historia para entrar (ver «Mínimo para entrar»).
- **Verificar cada repo** antes de añadir: comprobar `archived`, `stargazers_count` y `created_at` vía `gh api repos/owner/name`, y la fecha del último commit de la rama por defecto (no `pushed_at`).

## Formato de entrada

```markdown
- [Nombre](https://github.com/owner/repo) [![Stars](...)](stargazers) [![Last Commit](...)](commits) [![Language](...)](repo) [![License](...)](LICENSE) [![Tag](...)](url) - Descripción que empieza en mayúscula y termina con punto.
```

- La descripción **no debe empezar con el nombre** del proyecto.
- Máximo una línea por entrada.
- Validar con awesome-lint-extra: `python3 lint.py` o mediante el workflow de CI.
- Entradas en **orden alfabético** dentro de cada categoría.
- Categorías en **orden alfabético** en el índice y en el cuerpo del documento.
- Entradas en `DELETED.md` también en **orden alfabético** dentro de cada sección.

## Mínimo para entrar: rechazo directo

La lista recoge software con recorrido. Una PR que propone un repositorio sin estrellas ni historia se cierra sin más revisión. Se rechaza si, el día que se abre la PR, el repositorio cumple **cualquiera** de estas condiciones:

- Tiene **menos de 5 estrellas**.
- Tiene **menos de 3 meses**. Cuenta la fecha del primer commit; si el autor lo movió desde otro repositorio, cuenta la del original.
- Es **un volcado**: uno o dos commits del mismo día, o una copia de los datos de otra web sin el código que los genera.

La única excepción es el software publicado por un organismo oficial (un ministerio, una comunidad autónoma, un ayuntamiento, `ctt-gob-es`): entra aunque sea nuevo.

```bash
gh api repos/<owner>/<repo> --jq '{estrellas: .stargazers_count, creado: .created_at}'
# Fecha del primer commit: la última página de commits, de uno en uno.
# Las dos llamadas leen el mismo SHA, así un commit nuevo no mueve la última página.
# Para con error si una llamada falla, si hay más páginas sin enlace a la última o si no sale una fecha,
# en vez de leer la página 1, que tiene el commit más reciente.
# Solo lee la rama por defecto de este repositorio, ordenada por fecha de commit.
# Si el proyecto se movió, o su historia se reescribió o une varios repositorios, busca a mano el primer commit, en el original si lo hay.
(
  h=$(gh api "repos/<owner>/<repo>/commits?per_page=1" -i --jq '.[0].sha') || exit 1
  sha=$(printf '%s\n' "$h" | tail -n 1)
  n=$(printf '%s\n' "$h" | sed -n 's/.*[?&]page=\([0-9]*\)>; rel="last".*/\1/p')
  if [ -z "$n" ] && printf '%s\n' "$h" | grep -q 'rel="next"'; then
    echo "No hay enlace a la última página: no se puede saber el primer commit." >&2; exit 1
  fi
  d=$(gh api "repos/<owner>/<repo>/commits?sha=$sha&per_page=1&page=${n:-1}" --jq '.[0].commit.author.date // empty') || exit 1
  [ -n "$d" ] || { echo "No sale ninguna fecha: no se puede saber el primer commit." >&2; exit 1; }
  echo "$d"
)
```

Respuesta al cerrar, en pocas líneas y sin pedir estrella:

> Gracias por la propuesta. La cierro porque el repositorio todavía no llega al mínimo de la lista: 5 estrellas y 3 meses de historia. Lo que falta: <las estrellas, la historia o las dos cosas>. Hoy tiene <N> estrellas y su primer commit es del <fecha>. Cuando llegue al mínimo, vuelve a mandarlo y lo miro.

Si el motivo es que copia los datos de otro sitio sin el código que los genera, dilo en su lugar:

> Gracias por la propuesta. La cierro porque el repositorio es una copia de datos publicados en otro sitio, sin el código que los genera, y la lista no recoge copias de datos sin ese código. Si publicas ese código, vuelve a mandarlo y lo miro.

Si el motivo es que toda su historia son uno o dos commits del mismo día:

> Gracias por la propuesta. La cierro porque toda la historia del repositorio son uno o dos commits del mismo día, y la lista solo recoge proyectos con algo de recorrido. Cuando tenga más historia, vuelve a mandarlo y lo miro.

## Verificación antes de añadir

Si pasa el mínimo, comprobar:

- **Existe y es público**: el enlace de GitHub funciona y el repo no es privado.
- **No está archivado ni en solo lectura**: si lo está, la PR se cierra sin añadirlo a ningún sitio; `DELETED.md` solo recoge lo que estuvo en la lista.
- **Funciona hoy**: si **consume un servicio** (una API, una sede electrónica, una web que raspa), sigue haciéndolo. Si **no consume ninguno** (un validador, un formato, un dataset), su lógica o sus datos siguen siendo correctos. Antes de fusionar, se ejecuta o se coteja con la fuente oficial.
- **No es un duplicado**: cruzar con `README.md` y `DELETED.md`. Si ya hay una entrada mantenida que hace lo mismo, la nueva tiene que aportar algo más.
- **Calidad mínima**: tiene documentación (README) y no es un repositorio vacío o de pruebas.
- **La descripción es fiel**: el lenguaje, el alcance y las etiquetas de servicio coinciden con lo que hace el repositorio.

## Permanencia: qué se queda y qué se retira

Se queda lo que funciona y no tiene un sustituto mantenido en la lista. La reputación decide quién tiene que demostrar qué. Nada se retira sin que Sergio lo apruebe.

- **Archivado o en solo lectura**: se retira siempre.
- **Roto**: se retira, tenga la edad que tenga. Hay que enseñar el fallo: ejecutar el proyecto, comprobar que el servicio que consume ya no responde como espera o, si es un dataset, cotejar sus datos con la fuente oficial y señalar dónde no coinciden.
- **Sustituido**: si otra entrada mantenida de la lista hace lo mismo, la vieja se retira aunque tenga reputación. Va a `DELETED.md` con el enlace a la que la sustituye.
- **Sirve a un sistema retirado**: se retira aunque sea oficial.
- **Viejo**: más de 3 años sin commits en la rama por defecto (no `pushed_at`, que las ramas de bots rejuvenecen). Si no es ninguno de los casos anteriores:
  - **con reputación**, se queda mientras no se demuestre que está roto;
  - **sin reputación**, se queda solo si se comprueba que funciona hoy, ejecutándolo, cotejándolo con el servicio que consume o, si es un dataset, cotejando sus datos con la fuente oficial. Si no se puede comprobar, se retira.

Reputación es una de estas tres cosas:

- lo publica un organismo oficial;
- lo publica una organización conocida (rOpenSpain, Civio, Datadista, BSC/AINA…);
- tiene uso real visible: estrellas, forks, o descargas o dependientes en su registro (PyPI, npm, Packagist, RubyGems, CRAN, NuGet, crates.io). No hay un número fijo: se juzga caso a caso.

La revisión es trimestral. Lista las entradas archivadas y las que llevan más de 3 años sin commits, y revisa cada una con estos criterios; la tabla con la propuesta se le enseña a Sergio antes de mover nada a `DELETED.md`. Una entrada más reciente que resulta rota, ligada a un sistema retirado o sustituida por una entrada mantenida entra en una propuesta en cuanto se detecta. El filtro de 3 años solo marca cuándo se revisa la antigüedad.

## Pull requests y contribuciones

- Las PRs deben usar la plantilla en `.github/PULL_REQUEST_TEMPLATE.md`.
- **Obligatorio**: incluir en la PR la **URL del servicio, API o institución catalana** a la que el software da soporte.
- Plantillas de issues disponibles para sugerir proyectos (`anadir-proyecto.md`) y solicitar retirada (`retirar-proyecto.md`).

## Respuesta a quien abre una PR

Quien añade su proyecto a la lista quiere que se vea. Cuantas más estrellas tiene awesome-catalunya, más arriba sale en GitHub y más gente llega a cada entrada, así que darle una estrella también beneficia a quien contribuye. Toda respuesta a una PR de otra persona lo aprovecha:

- **Antes de responder, comprueba si ya le ha dado una estrella:**
  ```bash
  gh api --paginate repos/GeiserX/awesome-catalunya/stargazers --jq '.[].login' | grep -qix '<login>' && echo "ya tiene estrella"
  ```
  Si no sale nada (o `gh` falla), usa la frase condicional «si no le has dado ya una estrella».
- **PR fusionada:** da las gracias e invita a dar la estrella explicando qué gana con ello. Si ya la tiene, agradécela en vez de pedirla.
  > ¡Gracias, ya está en la lista! Si no le has dado ya una estrella ⭐ a awesome-catalunya, te animo a hacerlo: cuantas más estrellas tiene la lista, más arriba sale en GitHub y más gente descubre tu proyecto.
- **PR cerrada por no llegar al mínimo:** usa la respuesta de «Mínimo para entrar». No hace falta revisar el código ni los datos.
- **PR cerrada sin fusionar:** no se pide estrella por defecto, porque es pedir algo a cambio de un no. Solo se pide cuando le beneficia de verdad: la entrada pasa a otra de nuestras listas, o le invitas a volver cuando el proyecto cumpla los criterios.
- Responde en el idioma en que escribió el autor (castellano por defecto), tuteando y en pocas líneas.

## Estructura

- Secciones con `##`, subsecciones con `###`.
- Índice de contenido al principio entre comentarios `<!--lint disable/enable awesome-list-item-->`.
- Al final: sección Contribuir, Nota y Descargo de responsabilidad (como párrafos en negrita, no encabezados ##).

## Temas prohibidos

No se aceptan proyectos relacionados con: pornografía, contenido NSFW, loterías o apuestas, religión, política partidista.

## Difusión

- Notificar a los propietarios de repos abriendo un issue titulado «Listado en awesome-catalunya» con un breve mensaje en español (tuteo) ofreciendo retirar si lo prefieren. Solo 1 issue por organización/usuario — no spamear repos del mismo propietario.
- Publicar en comunidades catalanas tras alcanzar masa crítica.
- Enviar PR a [sindresorhus/awesome](https://github.com/sindresorhus/awesome) tras 30 días desde la creación del repo.

## Aprendizajes

- La Generalitat de Catalunya tiene la organización GitHub `gencat` con repos de utilidad real (Decidim, ICGC, Salut).
- `ConsorciAOC` tiene documentación de integración de servicios de administración electrónica catalana (Signador, eNotum, PCI, Representa, eFact).
- `AjuntamentdeBarcelona` tiene repos de participación ciudadana (Decidim Barcelona), ética digital y CKAN.
- `projectestac` es la organización de la XTEC con herramientas educativas activas (Agora, JClic, Odissea).
- `projecte-aina` es el Projecte AINA del BSC + Generalitat para tecnologías de lengua catalana.
- `Softcatala` es la ONG de software en catalán con repos muy activos (whisper-ctranslate2, open-dubbing, nmt-softcatala, catalan-dict-tools).
- `DiputacioBarcelona` tiene repos de datos abiertos municipales.
- `sentilo/sentilo` es la plataforma IoT nacida en Barcelona para sensores urbanos.

*Generated by [LynxPrompt](https://lynxprompt.com) CLI*

<!-- BEGIN BEADS INTEGRATION v:1 profile:minimal hash:6cd5cc61 -->
## Beads Issue Tracker

This project uses **bd (beads)** for issue tracking. Run `bd prime` to see full workflow context and commands.

### Quick Reference

```bash
bd ready              # Find available work
bd show <id>          # View issue details
bd update <id> --claim  # Claim work
bd close <id>         # Complete work
```

### Rules

- Use `bd` for ALL task tracking — do NOT use TodoWrite, TaskCreate, or markdown TODO lists
- Run `bd prime` for detailed command reference and session close protocol
- Use `bd remember` for persistent knowledge — do NOT use MEMORY.md files

**Architecture in one line:** issues live in a local Dolt DB; sync uses `refs/dolt/data` on your git remote; `.beads/issues.jsonl` is a passive export. See https://github.com/gastownhall/beads/blob/main/docs/SYNC_CONCEPTS.md for details and anti-patterns.

## Agent Context Profiles

The managed Beads block is task-tracking guidance, not permission to override repository, user, or orchestrator instructions.

- **Conservative (default)**: Use `bd` for task tracking. Do not run git commits, git pushes, or Dolt remote sync unless explicitly asked. At handoff, report changed files, validation, and suggested next commands.
- **Minimal**: Keep tool instruction files as pointers to `bd prime`; use the same conservative git policy unless active instructions say otherwise.
- **Team-maintainer**: Only when the repository explicitly opts in, agents may close beads, run quality gates, commit, and push as part of session close. A current "do not commit" or "do not push" instruction still wins.

## Session Completion

This protocol applies when ending a Beads implementation workflow. It is subordinate to explicit user, repository, and orchestrator instructions.

1. **File issues for remaining work** - Create beads for anything that needs follow-up
2. **Run quality gates** (if code changed) - Tests, linters, builds
3. **Update issue status** - Close finished work, update in-progress items
4. **Handle git/sync by active profile**:
   ```bash
   # Conservative/minimal/default: report status and proposed commands; wait for approval.
   git status

   # Team-maintainer opt-in only, unless current instructions forbid it:
   git pull --rebase
   git push
   git status
   ```
5. **Hand off** - Summarize changes, validation, issue status, and any blocked sync/commit/push step

**Critical rules:**
- Explicit user or orchestrator instructions override this Beads block.
- Do not commit or push without clear authority from the active profile or the current user request.
- If a required sync or push is blocked, stop and report the exact command and error.
<!-- END BEADS INTEGRATION -->

## Where the tracker syncs

This repo is public, so its tracker syncs only to the private remote named by `sync.remote` in `.beads/config.yaml`. The block above says sync uses "your git remote". Here that never means this GitHub repo. Don't add it as a Dolt remote and don't push `refs/dolt/*` to it.
