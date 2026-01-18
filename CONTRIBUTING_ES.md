¡Gracias por querer contribuir a OpenFisca! :smiley:

TL;DR: [Flujo de GitHub](https://guides.github.com/introduction/flow/),
[SemVer](http://semver.org/).

## Pull requests

Seguimos el [Flujo de GitHub](https://guides.github.com/introduction/flow/): todas
las contribuciones de código se envían a través de una solicitud de extracción (pull request) hacia la rama `main`.

Abrir una Pull Request significa que deseas que ese código sea fusionado (merged). Si solo quieres
discutirlo, envía un enlace a tu rama junto con tus preguntas a través del
canal de comunicación que prefieras.

### Revisiones por pares (Peer reviews)

Todas las pull requests deben ser revisadas por alguien distinto a su autor original.

> En caso de falta de revisores disponibles, uno puede revisarse a sí mismo, pero solo
> después de que hayan pasado al menos 24 horas sin trabajar en el código a revisar.

Para ayudar a los revisores, asegúrate de añadir a tu PR una **explicación clara en texto** de
tus cambios.

En caso de cambios que rompen la compatibilidad (breaking changes), **debes** dar detalles sobre qué características fueron
obsoletas (deprecated).

> También debes proporcionar pautas para ayudar a los usuarios a adaptar su código para ser
> compatible con la nueva versión del paquete.

## Anunciando cambios

### Número de versión

Seguimos la especificación de [versionado semántico](http://semver.org/): cualquier cambio
impacta el número de versión, y el número de versión transmite información de compatibilidad de API
**solamente**.

Ejemplos:

#### Incremento de parche (Patch bump)

- Arreglar o mejorar un cálculo ya existente.

#### Incremento menor (Minor bump)

- Añadir una variable al sistema fiscal y de beneficios.

#### Incremento mayor (Major bump)

- Renombrar o eliminar una variable del sistema fiscal y de beneficios.

### Registro de cambios (Changelog)

Los cambios en openfisca-paraguay deben ser entendidos por usuarios que no
necesariamente trabajan en el código. El Changelog debe ser por lo tanto lo más explícito
posible.

Cada cambio debe ser documentado con los siguientes elementos:

- En la primera línea aparece como título el número de versión, así como un enlace
  hacia la Pull Request que introduce el cambio. El nivel del título debe coincidir
  con el nivel de incremento de la versión.

> Por ejemplo:
>
> # 13.0.0 - [#671](https://example.com/repository/pull/671)
>
> ## 13.2.0 - [#676](https://example.com/repository/pull/676)
>
> ### 13.1.5 - [#684](https://example.com/repository/pull/684)

- La segunda línea indica el tipo de cambio. Los tipos posibles son:

- `Tax and benefit system evolution` (Evolución del sistema fiscal y de beneficios): Mejora de cálculo, arreglo o actualización.
  Impacta a los usuarios interesados en los cálculos.

- `Technical improvement` (Mejora técnica): Mejora de rendimiento, cambio en el proceso de instalación,
  cambio de sintaxis de fórmula... Impacta a los usuarios que escriben legislación y/o despliegan
  su propia instancia.

- `Crash fix` (Arreglo de caída): Impacta a todos los reutilizadores.

- `Minor change` (Cambio menor): Refactorización, metadatos... No tiene impacto en los usuarios.

- En el caso de una `Tax and benefit system evolution`, se deben especificar los siguientes
  elementos:

  - Los periodos impactados por el cambio. Para evitar cualquier ambigüedad, el día de inicio
    y/o el día final de los periodos impactados debe ser precisado. Por ejemplo,
    `desde 01/01/2017` es correcto, pero `desde 2017` no lo es, ya que es ambiguo:
    no está claro si 2017 está incluido o no en el periodo impactado.
  - Las áreas del sistema fiscal y de beneficios impactadas por el cambio. Estas áreas son
    descritas por las rutas relativas a los archivos modificados, sin la extensión
    `.py`.

> Por ejemplo:
>
> - Impacted periods: Until 31/12/2015.
> - Impacted areas: `benefits/healthcare/universal_coverage`

- Finalmente, para todos los casos excepto `Minor Change`, los cambios deben ser descritos
  de manera explícita con detalles dados desde la perspectiva del usuario: ¿en qué caso
  se notó un error o problema? ¿Cuál es la nueva característica disponible?
  ¿Qué nuevo comportamiento se adopta?

> Por ejemplo:
>
> - Details :
>   - These variables now return a yearly amount (instead of monthly):
>     - `middle_school_scholarship`
>     - `high_school_scholarship`
>   - _The previous monthly amounts were just yearly amounts artificially
>     divided by 12_
>
> o :
>
> - Details :
>
> * Use OpenFisca-Core `12.0.0`
> * Change the syntax used to declare parameters:
>   - Remove "fuzzy" attribute
>   - Remove "end" attribute
>   - All parameters are assumed to be valid until and end date is explicitly
>     specified with an `<END>` tag

Cuando una Pull Request contiene varios cambios distintos, se pueden añadir varios párrafos
al Changelog. Para ser formateados correctamente en Markdown, estos
párrafos deben estar separados por `<!-- -->`.
