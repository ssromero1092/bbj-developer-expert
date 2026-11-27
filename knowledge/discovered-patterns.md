# Discovered Patterns Index

Indice de patrones detectados en programas de referencia.

## Registro
| Patron | Tipo | Programas fuente | Evidencia | Confianza | Documento detalle |
|---|---|---|---|---|---|
| Listado externo guardado en MKEYED con upsert que respeta lo local | patron observado | defcomp.bbj | op 1 y op 7 funcionando en produccion | alta | references/file-io-patterns.md |
| Una rutina de acceso con N operaciones numeradas | patron observado | defcomp.bbj | 9 operaciones, firma unica | alta | references/purchases-integration-defontana.md |
| Pantalla hija con valores fijados por el padre via ENTER | patron observado | ADQ160.bbj 0012, 5406-5409 | probado en produccion | alta | references/ui-patterns.md |
| Dos grillas (listado ordenable y detalle) con variable de grilla activa | patron observado | CON214.bbj 21070-21084 | probado en produccion | alta | references/ui-patterns.md |
| Cuadratura contra el sistema externo con tolerancia | patron observado | ADQ160.bbj 40900-40940 | probado en produccion | alta | references/purchases-integration-defontana.md |
| Ingreso sin el servicio externo (degradacion controlada) | patron observado | CON214.bbj 24350-24356 | probado en produccion | alta | references/purchases-integration-defontana.md |
| Mantenedor simple grafico: EVENTOS + rutina por campo + botones en MENU_SUPERIOR + ultimo campo llama a GRABA | patron observado | MAE420.bbj 0041-0099, 9450-9570 | usado como plantilla de MAE330 (probado en servidor, OK) | alta | references/metacaracter-to-graphic-simple.md |
| Sub-flujo extra con panel de controles INVISIBLE en la misma ventana, mostrado con un boton | patron observado | MAE330.bbj 8000-8925 | probado en servidor, OK | alta | references/metacaracter-to-graphic-simple.md |
| Excel real con GEXCEL.bbj: temporal MKEYED con plantilla, WRITE por fila, CLOSE PRN, GEXCEL, abrir con Desktop | patron observado | programa de remuneraciones (referencia), MAE330 21000-21050, 30920-30950, 31000-31075 | probado en servidor, OK | alta | references/metacaracter-to-graphic-simple.md |
| Mantenedor sin periodo: se quitan el combo de periodo y GPERIODO del encabezado | patron observado | MAE340 (conversion) | 2da conversion; probado en servidor | media | references/metacaracter-to-graphic-simple.md |
| Codigo inexistente en un maestro -> alta directa con CALL al programa de alta (sin boton Crear) | patron observado | MAE330 0925, MAE340 0535 | MAE330 probado antes en ADQ160/MAE420; MAE340 probado en servidor | alta | references/metacaracter-to-graphic-simple.md |

## Tipos permitidos
- patron observado
- convencion probable
- capacidad BBj verificada
- hipotesis
- excepcion
