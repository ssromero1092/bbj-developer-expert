# Workflow: Propose Change

## Objetivo
Construir propuesta tecnica sin editar archivos.

## Estructura obligatoria
1. Comprension del requerimiento.
2. Comportamiento actual.
3. Comportamiento esperado.
4. Archivos y rutinas a afectar.
5. Cambios propuestos (minimos y localizados).
6. Dependencias y supuestos.
7. Riesgos y regresiones posibles.
8. Pruebas recomendadas.
9. Solicitud de autorizacion explicita.

## Seccion obligatoria adicional (si hay campo con ayuda)
- Matriz de dependencias del maestro:
	- Campo UI (.arc): ID edit + ID toolbutton + posicion
	- Campo logico (.bbj): callback, rutina de ayuda, validacion, asignacion
	- Maestro: archivo, key/knum, largo de codigo, campo descripcion, formato de salida
	- Impacto de persistencia: si solo consulta o si tambien graba en cabecera/detalle
	- Riesgo por layout: campos sin layout confirmado

Sin esta matriz, la propuesta queda en estado incompleta.

## Criterios de calidad
- Cada cambio debe estar respaldado por evidencia del codigo o por requerimiento explicito.
- Distinguir hechos verificados vs hipotesis.
- No proponer re-arquitecturas sin justificacion fuerte.
