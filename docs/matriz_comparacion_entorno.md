# Matriz de comparacion tecnica del entorno

Completa esta tabla despues de terminar el artefacto.

| Criterio | Pregunta guia | Valoracion 1 a 5 | Justificacion tecnica |
|---|---|---:|---|
| Funcionalidad | ¿El entorno permitio abrir el proyecto, editar codigo, ejecutar scripts, leer CSV y generar reportes? | 5 | El proyecto corre con Python estandar, se ejecuta el flujo completo (00/01/02/03) y se genera `output/reporte_rural.txt`. |
| Compatibilidad | ¿Funciono con el equipo disponible, el sistema operativo y Python? | 5 | Funciona en Windows 11 con Python 3.14.3 y archivos CSV locales sin dependencias externas. |
| Costo | ¿Se pudo trabajar con herramientas gratuitas o de bajo costo? | 5 | Uso de VS Code y librerias estandar de Python. No se instalaron paquetes obligatorios. |
| Facilidad de uso | ¿Fue facil encontrar terminal, archivos, errores y resultados? | 4 | Los errores se mostraron en la terminal y la estructura de carpetas (data/src/output) facilito ubicar fallos; requirio corregir rutas/variables. |
| Rendimiento | ¿El entorno pudo procesar miles de registros sin bloquearse? | 5 | Se procesaron 8205 registros; el script completó correctamente y las pruebas pasaron. |
| Depuracion | ¿Los mensajes de error ayudaron a corregir el programa? | 5 | Los mensajes (FileNotFoundError, NameError, KeyError, ValueError) guiaron correcciones por bloque hasta pasar pruebas. |
| Organizacion | ¿La estructura de carpetas facilito comprender el proyecto? | 5 | Separacion clara: `data/` para insumos, `src/` para scripts, `output/` para resultado y `evidencias/`/`docs/` para documentacion. |
| Recomendacion final | ¿Recomendarias este entorno para proyectos similares? | 5 | Es adecuado para proyectos educativos de lectura/validacion de CSV y generacion de reportes con depuracion incremental. |

