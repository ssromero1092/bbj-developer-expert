# BBj Database Patterns

Patrones de acceso a datos observados en el entorno del usuario.

## Que registrar
- Apertura de archivos/tablas y selecciones de datos.
- Uso de SQL, cursores, claves e indices cuando aplique.
- Operaciones de insercion/actualizacion/eliminacion.
- Manejo de errores de base de datos.
- Estructura del maestro usado por ayudas UI: key/knum, largo de codigo, posicion de descripcion y layout de registro.

## Ficha de patron
- Nombre:
- Programa fuente:
- Seccion/rutina:
- Fragmento minimo:
- Riesgos:
- Confianza:

## Regla
No asumir motores externos (MySQL/PostgreSQL/etc.) sin evidencia.
No asumir layout de archivo maestro sin formato verificable.

## Nota sobre formatos externos (.doc/.docx)
Si el layout llega en Word y no es legible como texto en el entorno de analisis:
- Marcar la estructura como pendiente de confirmar.
- Solicitar version legible (txt/markdown/pdf) o tabla de campos exportada.
