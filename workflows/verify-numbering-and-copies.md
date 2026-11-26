# Workflow: Verificar numeracion y mantener copias

## Cuando usarlo
Despues de **cada** edicion de un programa BBj con numeracion interna, y antes de entregarlo.

## Pasos
1. Ejecutar `tools/check_bbj_numbering.py <archivo>` sobre cada `.bbj` tocado.
2. Si informa saltos a lineas inexistentes, comprobar si **ya faltaban en el original** (comparar con la copia en uso). Solo los nuevos son defecto del cambio.
3. Al borrar lineas (por ejemplo trazas de depuracion), buscar antes si algun `DOM=`/`ERR=`/`GOTO` apunta a ellas. Si es destino, dejarla como `REM`.
4. Al insertar una linea, usar un **hueco numerico libre** entre sus vecinas; no repetir un numero ni dejarla fuera de orden.
5. Resumen final: "correlacion de numeracion verificada" y que se probo / que no.

## Regla de dos copias
Cuando existe una **copia de trabajo** (en git) y una **copia en uso** (servidor):
- Editar solo la copia de trabajo.
- Leer la copia en uso solo para comparar.
- Para decir que esta "al dia", comparar **byte a byte** (`cmp`) y no por fecha: la hora de modificacion puede confundir.
- Si la copia en uso tiene una version **mas nueva** de un archivo (por ejemplo de otro frente de trabajo), no sobrescribirla: revisar la diferencia antes de cualquier commit.

## Commits
Un commit con los programas y otro con la documentacion. No hacer `commit` ni `push` hasta que el usuario lo pida.
