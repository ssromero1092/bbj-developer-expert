# Workflow: Analyze Existing Program

## Objetivo
Analizar programas BBj/.arc disponibles para entender comportamiento actual y dependencias.

## Pasos
1. Identificar archivo principal y puntos de entrada/salida.
2. Mapear flujo general y rutinas clave.
3. Registrar llamadas a otros programas y recursos externos.
4. Identificar operaciones de lectura/escritura, SQL y validaciones.
5. Detectar manejo de errores y controles de concurrencia.
6. Marcar huecos por falta de archivos o contexto.

## Analisis obligatorio para campos con ayuda (maestros)
Aplicar cuando exista boton/lupa y llamadas GZOOM o similares.

1. Identificar IDs del edit y del toolbutton en el .arc.
2. Ubicar callbacks e instanciacion de controles en .bbj.
3. Ubicar rutina que abre ayuda (GZOOM/GZOOMWD/GZOOMLH) y su archivo maestro destino.
4. Verificar lectura por KEY/KNUM y formato esperado del dato retornado.
5. Verificar dependencias de estructura del maestro (largo, posicion, key, descripcion).
6. Registrar claramente lo faltante si no existe formato de archivo confiable.

## Insumos minimos requeridos
- Pantalla .arc
- Programa .bbj relacionado
- Formato de archivo maestro (layout)

Si el layout viene en Word binario no legible, solicitar version en texto/markdown/PDF legible antes de cerrar propuesta tecnica.

## Clasificacion de hallazgos
- Patron observado.
- Convencion probable.
- Capacidad BBj verificada.
- Hipotesis pendiente.
- Excepcion al patron.

## Entregable
Resumen tecnico corto + lista de evidencias por rutina/seccion.
