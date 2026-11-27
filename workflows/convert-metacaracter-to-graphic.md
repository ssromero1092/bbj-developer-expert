# Workflow: Convertir un programa de metacaracter a grafico (BBj)

## Cuando se usa
El usuario entrega un programa BBj que corre en **metacaracteres** (pantalla de texto, `INPUT`/`PRINT @(x,y)`) y pide pasarlo a **grafico** (ventana, botones, controles `.arc`) **sin perder la logica de negocio**. Ejemplo ya hecho: MAE330, ver `references/metacaracter-to-graphic-simple.md`.

## Tipos de pantalla (a grandes rangos)
| Tipo | Ejemplos | Estado en la skill |
|---|---|---|
| 1. Mantenedor/ingresador **simple** (campos en cadena, un registro a la vez) | MAE330, MAE420 | **Documentado**: `references/metacaracter-to-graphic-simple.md` |
| 2. Mantenedor/ingresador **complejo** (grillas, totales, funciones mas elaboradas) | orden de compra, registro de facturas (ADQ160, CON214) | PENDIENTE: hay patrones de grilla en `references/ui-patterns.md`, falta documentar la conversion |
| 3. **Informes y reportes** (ventanas de listado, impresion, Excel) | listados | PENDIENTE (en el tipo 1 solo se conecto el listado existente al boton Imprimir) |

Primero clasificar la pantalla. Si es tipo 2 o 3, decirlo al usuario: la receta aun no esta documentada y hay que construirla con el, anotando lo aprendido aqui.

## Reglas del trabajo (acordadas por el usuario)
1. Copiar `metacaracter/pgms/X.bbj` a `pgms/X.bbj`. **Editar solo la copia de `pgms/`**; `metacaracter/` no se toca nunca.
2. Crear `brc/esp/x.arc` (nombre en minusculas).
3. Mantener la logica de negocio y las lineas del programa original (mismas lecturas, escrituras, validaciones y numeracion donde se pueda). Si el usuario no conoce el programa, **se respeta la logica tal como esta**.
4. Mantener la armonia visual y los patrones de un programa grafico ya hecho que el usuario entregue como referencia (en MAE330 fue MAE420: `.bbj` + `.arc`).
5. **No usar `BBTranslator` ni `Translator!.getTranslation(...)`**: esta deprecado y no funciona en ningun sistema BBj de la empresa. Mensajes con texto directo: `MJ=MSGBOX("Texto",48+262144,"Mensaje")`. No copiar `use ::bbtranslator` ni `Translator!=` aunque la referencia los traiga.
6. Los `.arc` no llevan numeros en las etiquetas ("1.", "2."): solo el nombre del campo.
7. Cada decision que el usuario tome se anota en la carpeta de memoria del proyecto (hecho verificado vs hipotesis).
8. REVIEW FIRST: analizar, proponer y preguntar **antes** de escribir. Commit y push solo si el usuario lo pide.

## Pasos
1. **Entender**: resumir que hace el programa original (archivos, claves, flujo de captura, opciones de menu, impresion).
2. **Inspeccionar**: leer el original completo y la referencia grafica (`.bbj` + `.arc`). Correr `tools/check_bbj_numbering.py` sobre el original y anotar los saltos a lineas inexistentes que ya trae (no son del cambio; no "arreglarlos" sin autorizacion).
3. **Preguntar** al usuario lo que no se pueda saber del codigo (lista en la receta, seccion "Preguntas tipicas").
4. **Proponer**: tabla campo por campo (linea original -> control/id -> rutina nueva), botones, ayudas y lo que queda "sin verificar". **Listar los defectos del original** (saltos a lineas inexistentes, rotulos repetidos, ortografia, canales que se cierran sin abrirse) y preguntar si se corrigen; preguntar tambien si lleva periodo y si hay que agregar Excel.
5. Esperar autorizacion e implementar (`workflows/implement-approved-change.md`).
6. Verificar: numeracion con la herramienta, y que **todo control usado en el `.bbj` exista en el `.arc`** (ver receta).
7. Registrar en la memoria del proyecto y, si se aprendio algo general, en esta skill.
8. Cerrar con `workflows/review-changes.md`; indicar que se debe **probar en el servidor** (nada se asume funcionando).
