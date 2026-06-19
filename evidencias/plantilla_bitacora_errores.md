# Bitacora tecnica de errores

## Datos del estudiante

Nombre: (completa con tu nombre)
Grupo: (completa con tu grupo)
Fecha: 2026-06-16
Entorno utilizado: VS Code + Python (scripts en terminal)
Sistema operativo: Windows 11

## Registro de errores corregidos

| Nº | Error encontrado | Mensaje mostrado por Python | Linea o bloque | Causa identificada | Solucion aplicada | Como verifique que funciono |
|---:|---|---|---|---|---|---|
| 1 | FileNotFoundError | No such file or directory: ...\data\produccion.csv | Bloque 1 (rutas) | Ruta al CSV mal nombrada y carpeta de salida mal escrita | Cambié a `DATA_FILE = .../data/produccion_rural.csv` y `OUTPUT_FILE = .../output/reporte_rural.txt` | `python src/02_reporte_rural_CON_ERRORES.py` avanzó al siguiente error y luego generó el reporte |
| 2 | NameError (variable) | NameError: name 'registros' is not defined | Bloque 2 (`leer_csv`) | `leer_csv()` retornaba una variable inexistente | Cambié el retorno a `return filas` | El script ya pudo ejecutar `limpiar_registros()` |
| 3 | KeyError (columna) | KeyError: 'cantida' | Bloque 5 (limpieza) | Nombre de columna incorrecto | Cambié a `registro['cantidad']` | Se evitó el KeyError y el flujo continuó |
| 4 | ValueError (float) | ValueError: could not convert string to float: '' | Bloque 3/5 (conversion) | Conversión numérica sin manejar vacíos | `convertir_a_numero()` ahora retorna `None` si el valor está vacío/no convertible y en limpieza se marca registro inválido | Ya no falló por conversión y el conteo de inválidos se mantuvo |
| 5 | TypeError (comparación) | TypeError: '<' not supported between NoneType and int | Bloque 5 (validaciones) | Se comparaba `None < 0` | Ajusté validación: si `cantidad` o `precio` es `None` => inválido | Se pudo calcular resumen |
| 6 | NameError (función) | NameError: name 'analizar_productos' is not defined | Bloque 9 (main) | Llamada a función con nombre incorrecto | Cambié `analizar_productos` por `analizar_por_producto` | El script generó el reporte |
| 7 | ValueError (max con iterable vacío) | max() iterable argument is empty | Bloque 4/7 (fechas + limpieza) | `fecha_valida()` usaba formato incorrecto => todos inválidos | Cambié `fecha_valida` a formato `'%Y-%m-%d'` | `python src/03_pruebas_reporte.py` pasó |
| 8 | Error lógico variable | (retorno finca) (derivado del bloque 7) | Bloque 7 (`calcular_finca_mayor_ingreso`) | Variable mal nombrada en return | Retorné `finca_mayor` y el ingreso correspondiente | Pruebas confirmaron que la finca con mayor ingreso se identificó |

## Reflexion tecnica

1. ¿Cual fue el error mas dificil de corregir?
- La validación de fechas, porque un formato incorrecto hacía que la limpieza invalidara casi todos los registros y luego ocurrían fallos posteriores (por ejemplo, `max()` sobre diccionario vacío).

2. ¿Que aprendiste sobre lectura de errores en la terminal?
- Que conviene leer el traceback completo: identifica con precisión el archivo, la línea y la causa (FileNotFoundError, NameError, KeyError, ValueError, TypeError) para corregir el bloque exacto.

3. ¿Por que es importante probar despues de cada cambio?
- Porque algunos errores no se ven hasta corregir otros. Probar después de cada ajuste confirma que el nuevo cambio no rompe el flujo y avanza hacia el siguiente fallo real.

4. ¿Que ventaja tiene organizar el proyecto en carpetas?
- Facilita ubicar rutas correctas (data/src/output) y separar responsabilidades; así la depuración es más rápida y menos propensa a errores.

