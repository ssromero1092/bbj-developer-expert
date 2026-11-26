# Trampas frecuentes en BBj / Business BASIC

Origen: revisión de `integracion.bbj`, `DAIRE_ERP.bbj`, `DAIRE_ERP_LOGIN.bbj` y `PRO240.bbj`. Las entradas marcadas *(verificar)* dependen de la versión de BBj y no se han probado contra el servidor del usuario.

## Literales de string
- BBj **no interpreta `\` dentro de literales**. `"\\n"` son 3 caracteres (`\`,`\`,`n`), no un salto de línea. Para JSON usa `CHR(92)`, `CHR(34)`, `CHR(10)`.
- Una comilla dentro de un literal se escribe duplicada: `"a""b"` = `a"b`.
- Patrón peligroso: `WHILE POS(X$=S$) ... S$=reemplazo_que_contiene_X$ ... WEND`. Si el reemplazo contiene el carácter buscado, el bucle **no termina**. Recorre el string una vez, copiando a un buffer de salida (como hace `escapeForDoubleQuotes` en `DAIRE_ERP.bbj`).
- JSON válido exige escapar también tab (`CHR(9)`) y demás caracteres < 0x20.

## Depuración olvidada
- `ESCAPE` detiene el programa en producción. Buscar con Grep `-i "escape"` antes de entregar (ojo con `escape;` en minúscula, ej. `integracion.bbj 2220`).
- `PRINT "DEBUG..."` en programas llamados desde pantallas con `@(x,y)` / `'WINDOW'` ensucia la pantalla; usar `java.lang.System.out.println` o un log.
- No loguear tokens `Bearer` ni payloads completos.

## Variables y tipos
- Usar una variable numérica nunca asignada provoca error 11 (*verificar código exacto*). Ej.: `GOSUB 3200` sin asignar `NUM_IN` antes.
- Variable de retorno que solo se asigna en algunas rutas (ej. `ESTADO_API` en `PRO240 9500`) y se consulta después en todas.
- `ENTER` con `$` vs `!`: pasar `TOKEN_API$` a un parámetro `token!` mezcla string y objeto. *(verificar si BBj lo convierte o lanza error de tipo)*. Mantener el mismo sufijo en llamador y llamado.
- `CALL` pasa variables por referencia: lo que el llamado modifica se ve en el llamador.
- `ENTER` sin `ERR=*next` en un programa que se llama varias veces: lanza **error 36 ("ENTER already executed in this program")** y deja el programa detenido en consola. Confirmado en `publicos/linux_windows.bbj` (línea 3): se resolvió con `enter origen$,destino$,salida_ok,err=*next`. Usar siempre `ERR=*next` en el `ENTER` de programas reutilizables (como ya hacen `integracion.bbj`, `DAIRE_ERP.bbj`).
- Un literal en un parámetro de `CALL` (p. ej. `...,destino$,0`) no recibe de vuelta lo que el llamado asigna; para leer un resultado hay que pasar una variable.

## INPUT
- La lista de un `INPUT` no acepta expresiones: `INPUT (0)...,""+X$(A,B),*` da **ERROR=20 (Syntax error)** (confirmado en `PRO240 9635`, 2026-11-13). Para mostrar texto variable, usar `PRINT` y luego `INPUT (0,...)@(col,fila),*`. Un substring suelto (`X$(A,B)`) sí compila en `INPUT`, pero se interpreta como destino de lo tecleado, no como texto a mostrar *(sospecha, no confirmada)*.

## Archivos keyed
- `READ (ch,KNUM=0,KEY=k$,DOM=lbl)` sin lista de variables **consume** el registro si la clave existe exacta; si no existe, `DOM` posiciona en la siguiente clave mayor. Es el patrón usado para recorrer detalle (`CLAVE$+STR(I:"000")`).
- Toda ruta de error que salga con `GOTO` debe cerrar los canales abiertos con `UNT`. En `integracion.bbj` los `CLOSE` (0130) solo corren en el camino feliz.
- Registros numéricos se leen en variable string y viceversa; el orden de campos manda. Verificar siempre contra el `WRITE` correspondiente (en PRO240: `WRITE (VTAEFAC)` 1410, `WRITE (VTAGFAC)` 1520).

## Estructura de rutinas
- Una misma rutina de trim copiada 6 veces (1071, 3031, 3221, 3321, 3511) y otra sin usar (3800). Unificar con `GOSUB 3800` (entrada `TXT_TMP$`, salida `TXT_TRIM$`).
- `IF TCB(13) THEN EXIT ELSE RELEASE` al final: distingue si fue `CALL`ado. Mantenerlo.
- `ERR=` en `CALL` captura errores no atrapados del llamado, pero solo recibe el número; usar `ERRMES(-1)` *(verificar)* para el texto de excepciones Java.

## HTTP (BBWebClient)
- Códigos HTTP (200/201) no son "0 = OK". No compararlos con `<>0` para decidir éxito.
- Un 200 puede traer `{"estado":false}` en el cuerpo: parsear y validar.
- Revisar timeout y reintento ante 401 (token vencido). *(verificar si `BBWebClient` expone timeout en la versión del entorno)*
- Construir JSON concatenando strings exige escapar también en credenciales (`DAIRE_ERP_LOGIN.bbj` 28). Preferir `org.json.JSONObject` (ya usado en el login) para construir y parsear.
- El header `Acces-Control-Allow-Origin` es de respuesta (y está mal escrito); no aporta en un request.
