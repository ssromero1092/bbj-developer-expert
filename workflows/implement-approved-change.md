# Workflow: Implement Approved Change

## Precondicion
Solo ejecutar cuando el usuario autorice explicitamente la implementacion.

## Pasos
1. Confirmar alcance exacto aprobado.
2. Enumerar archivos a modificar antes de editar.
3. Aplicar cambios minimos, manteniendo estilo y convenciones locales.
4. Evitar tocar codigo no relacionado.
5. Si surge impacto no aprobado, detener y consultar.
6. Registrar cada cambio con motivacion tecnica.

## Checklist obligatoria: numeracion interna BBj
Aplicar cuando el programa tenga numeros de linea escritos en el codigo.

1. Identificar rango de lineas numeradas a intervenir (inicio/fin).
2. Validar que los nuevos numeros mantengan orden ascendente dentro del bloque.
3. Validar correlacion con el patron del archivo (saltos, huecos y estilo de numeracion existente).
4. Validar que no se dupliquen numeros de linea en la misma seccion.
5. Verificar que GOTO/GOSUB/RETURN sigan apuntando a destinos correctos tras los cambios.
6. Registrar en el resumen final que la correlacion de numeracion fue verificada.

## Restricciones
- No operaciones destructivas.
- No acceso a servidores externos.
- No cambios de nombres/tablas/campos sin necesidad y aprobacion.
- No usar lineas del IDE como unica referencia cuando exista numeracion interna BBj.
