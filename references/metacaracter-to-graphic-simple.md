# Receta: mantenedor simple de metacaracter a grafico

Origen: conversion de MAE330 (mantencion de dosificacion de productos) usando MAE420 como patron grafico. **Estado: implementado y probado por el usuario en el servidor, todo funciona OK** (2026-11-26).

Aplica a pantallas donde se captura una clave (area, grupo, producto...), se lee/graba **un registro** y hay unas pocas opciones (modificar, eliminar, copiar, listar). Ver el tipo en `workflows/convert-metacaracter-to-graphic.md`.

## 1. Que se reutiliza sin cambios
| Bloque | Como |
|---|---|
| Cabecera (`use java.io...`, `ENTER LLAMADA`, `GOSUB 12000`) | Igual |
| Abrir archivos (`5600-5800`) y cerrar (`CIERRA`) | Igual (se agregan los canales nuevos que haga falta cerrar) |
| `lee_parametros` (`12000-12203`) | Igual, **pero sin** `use ::bbtranslator` ni `Translator!=` |
| `READ/WRITE/REMOVE/EXTRACT` sobre los archivos de negocio | Igual: misma clave y mismo orden de campos |
| Recorridos con 2do canal (copiar, actualizar) | Igual |
| Listado/Excel (`29000-30950`) | Igual; se conecta al boton Imprimir y se cambian solo 4-5 lineas (ver 4) |

## 2. Que se reemplaza (tabla de equivalencias)
| En metacaracter | En grafico |
|---|---|
| `PRINT @(x,y),"Etiqueta :"` | `STATICTEXT` en el `.arc` (sin numeros de lista) |
| `INPUT (0,SIZ=n)@(x,y)... campo$` | `EDIT` en el `.arc` + callback `ON_EDIT_KEYPRESS` -> `EVENTOS` |
| `CTL=3` (F3 = ayuda) | tecla 333 en `EVENTOS` (`CTW=3`) o boton lupa (`TOOLBUTTON` con `LUPA.bmp`, `ON_TOOL_BUTTON_PUSH`) |
| `CTL=1` (F1 = retroceder/fin) | boton **Cancelar** (`LIMPIAR_OBJ`) y **Salir** (`SALIDA`) |
| `CTL=4` y otros F extra (copiar, actualizar, listar) | **botones extra** en `MENU_SUPERIOR` (ids 137, 138...) |
| `INPUT ... "ESTA CORRECTO, [ENTER] SI / [N] NO"` | `MSGBOX("Esta Correcto ?",4+32+262144,"Mensaje")`; respuesta 7 = No |
| Opciones `M`/`E`/`A` tras mostrar el registro | Botones Guardar / Borrar / Actualizar |
| Menu "numero a modificar [1-n]" | **Se elimina**: con el registro existente (`SW=1`), Enter en un campo modificado llama a `GRABA` directo (como el original, que saltaba al menu con `IF SW=1 THEN GOTO 2300`) |
| `PRINT @(x,y),'CL',VALOR` para mostrar | `Editc_n!.setText(...)` / `static_n!.setText(...)` |
| Limpiar zona de pantalla | `PRINT(GUI)'CLRTITLE'(ids...)` y `'DISABLE'(ids...)` |
| `GOTO linea_anterior` al retroceder | Ya no hay retroceso por campo: Cancelar limpia todo (`LIMPIAR_OBJ`) |

## 3. Esqueleto del `.bbj` grafico (de MAE420)
Orden de bloques: cabecera -> `GOSUB 5000` (PANTALLA), `5200` (PERIODO), `5600` (archivos) -> `PRINCIPAL:` (callbacks + `process_events`) -> `EVENTOS:` -> rutinas por campo -> `GRABA`/`ELIMINA`/otras acciones -> `PANTALLA` -> `MENU_SUPERIOR` -> errores/salida -> `INSTANCIAR_OBJ` -> colores -> `ERROR_OBJ` -> impresion.

### EVENTOS (patron MAE420 0041-0099)
- 1er `SWITCH OBJ`: por cada EDIT define `CTW=0,largos=n` y mira la tecla: Enter (13) valida; F3 (333) con campo que tiene ayuda pone `CTW=3`; cualquier otra tecla `exitto principal`. Las lupas (`TOOLBUTTON`) ponen `CTW=3` y apuntan al EDIT (`obj=111`).
- 2do `SWITCH OBJ`: lee `CTRL(GUI,OBJ,1)` en `X0$` y hace `GOSUB` a la rutina del campo.
- Cada rutina de campo: (si `CTW=3` abre la ayuda) -> valida/lee maestro -> `setText` -> habilita y da foco al siguiente (`PRINT(GUI)'ENABLE'(n),'FOCUS'(n)`). Si `SW=1` (registro existente) -> `GOSUB GRABA`.
- **El ultimo campo del flujo llama a `GOSUB GRABA`** al dar Enter (pedido del usuario; en el original tambien pasaba directo a la confirmacion). `GRABA` pide la confirmacion con `MSGBOX`.
- `GRABA` revalida lo que hay en pantalla (rutina `CAPTURA`) antes de escribir, porque el usuario puede cambiar un campo sin pulsar Enter.

### Botones del menu superior (MENU_SUPERIOR, patron MAE420 9450-9570)
Ayuda 131, Cancelar 132, Salir 134, Guardar 135, Borrar 133, Imprimir 136, mas los propios (Copiar 137, Actualizar 138). `addMenuButton(id,x,2,100,40,"Texto")`, fuente Sans Serif 10, fondo blanco, imagen `NOMBRE.bmp`. Si el `.bmp` no existe en el servidor el boton queda sin icono.

### IDs reservados del encabezado (no reusar)
`101` ventana y listbutton de periodo, `118` listbutton impresora (invisible), `130` color chooser, `131-138` botones, `219`, `220` (banda blanca), `300` (texto "Periodo"), `7001` barra de estado. Campos propios desde `102` en adelante sin chocar con esos.

## 4. Impresion y Excel
- Se conecta el listado existente al boton Imprimir: `GOSUB ABRE_IMPRE_VIEW` (patron MAE420 11290-11660) en lugar de abrir `P2`; `LLENA_DISPO` -> `CALL "GIMPRIME.bbj",118,GUI` carga la lista de impresoras.
- Ajustar `COLS=` de `ABRE_IMPRE_VIEW` al ancho del listado (MAE420 usa 170; MAE330 necesita 200 porque imprime 190 columnas). Verificado en el servidor (se ve bien).
- Mensajes de `INPUT ... OBSERVACION` del listado/Excel -> `MSGBOX` con texto directo.

## 5. Ayudas (GZOOM) en grafico
Regla del usuario: usar **la misma ayuda que usa el programa original**.
| Original | En grafico (visto funcionando en otros programas del usuario) |
|---|---|
| `GZOOMLH` (productos) | `GOSUB DISWIN; CALL "GZOOMLH.bbj",2,"",MAEPROD,10,2,X0$,"","MAESTRO ..."; GOSUB ENWIN` (ADQ160 2821). **No** cambiarlo por GZOOMWD1. |
| `GZOOM2` (areas/centros de costo) | `CALL "GZOOM2.bbj",20,1,50,22,"< TITULO >",ARCH,0,X0$,PREFIJO$,LLAVE,"0102","0230","F0402  ",Window!,sysgui!,1,myAPI!` (ADQ160 3215, MAE420 4145) |
| `GZOOM` (tabla `MAETABL` por codigo) | `GOSUB DISWIN; CALL "GZOOMWD1.bbj",20,1,50,22,"O.CTITULO",MAETABL,LLAVE,X0$,"010315020130","01^35",EXCL$,Window!,sysgui!,1,myAPI!; GOSUB ENWIN` (patron MAE420 1315). Probado en el servidor con la tabla "35" de objetivos. |
| Alta de maestro inexistente `CALL "MAE108"` | `sysgui!.flushEvents(); CALL "MAE108.bbj",1,""; PRINT(GUI)'CONTEXT'(0),'FOCUS'(id)` (y `MAE105`, `MAE109`, `MAE410` segun el maestro) |
`INCL$`/`EXCL$` se dejaron en `""`: no se vio donde otros programas los inicializan; en el servidor funciono asi.

## 6. Sub-flujos extra (copiar, actualizar)
- En MAE330 el sub-flujo de **copia** (otro conjunto de campos) se resolvio con un **panel de controles `INVISIBLE` en la misma ventana** (ids 181-196) que se muestra/oculta con `Window!.getControl(n).setVisible(0/1)` al pulsar el boton Copiar; Cancelar lo cierra. Motivo: el cambio de contexto de una 2da ventana (como la 102 de ADQ160) no estaba verificado en este entorno. `setVisible` en este uso **funciona** (probado en el servidor).
- Una rutina de actualizacion masiva (recorre todo el archivo por el 2do canal) debe **informar cuantos registros cambio** (`Registros actualizados : N`) para que el usuario pueda ver que paso.

## 7. Verificaciones obligatorias antes de entregar
1. `python -I tools/check_bbj_numbering.py pgms/X.bbj`: solo deben aparecer saltos que **ya existian** en el original (anotarlos).
2. Todo `getControl(n)` del `.bbj` existe como control en el `.arc` (script simple que cruce ids).
3. Archivos `.bbj` y `.arc` en ASCII con LF (igual que los de referencia).
4. Ninguna referencia a `Translator`/`getTranslation`.
5. Etiquetas del `.arc` sin numeros.
6. Declarar "correlacion de numeracion verificada" y que **no se probo en servidor** salvo que el usuario lo diga.

## 8. Preguntas tipicas al usuario (antes de implementar)
- Como se llegaba al listado/Excel en el original (si el `GOSUB` esta roto) y si se conecta al boton Imprimir.
- Los sub-flujos (copiar, actualizar...): siguen en la pantalla y con boton propio?
- Las teclas F extra que llaman a lineas inexistentes: se omiten?
- Hay filtro de usuarios? (el de MAE420 era de MAE420, no se copia).
- Rutas fijas del original (p. ej. ruta de pruebas en PC local): se dejan igual?
- Nombres de los `.bmp` de botones nuevos.

## 9. Trampas encontradas al hacerlo
- Los programas de metacaracter traen saltos a lineas inexistentes (`GOSUB 20000`, `ERR=10400/10500/10300`): hay que **reponer** las rutinas de error de la referencia (10300-10600, 11000) y `DEPURAR` (20000) para que no queden rotos; el verificador solo debe marcar los que ya traia el original.
- Cuidado con el orden de los `IF ... THEN ... ELSE ... FI` al meter `GOSUB GRABA`: usar `FI`.
- Al generar archivos con scripts: comandos muy largos fallan (`ENAMETOOLONG`); guardar el script en un archivo y ejecutarlo. Con `sed`, usar `|` como delimitador si el texto lleva `/`.
- En un repo nuevo, `git commit` falla sin identidad: configurar `user.name`/`user.email` **solo en ese repo**.
- Un `git add` previo a un commit fallido deja archivos en el area de preparacion y entran en el siguiente commit: revisar `git status` antes de commitear programas y documentacion por separado.
