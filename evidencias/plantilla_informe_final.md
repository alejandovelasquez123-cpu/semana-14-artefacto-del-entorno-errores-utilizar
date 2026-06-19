# Informe final del artefacto

## 1. Nombre del proyecto

Artefacto del entorno: reporte rural automatico.

## 2. Problema contextual

El proyecto procesa miles de registros de produccion rural almacenados en un CSV (finca, producto, cantidad, precio unitario, fecha y observaciones). El objetivo es generar un reporte automatico que permita:

- calcular el total producido por producto;
- calcular el ingreso estimado por producto;
- identificar la finca con mayor ingreso;
- contabilizar registros invalidos (problemas de calidad de datos).

## 3. Entorno utilizado

- IDE o editor: Visual Studio Code
- Version de Python: 3.14.3
- Sistema operativo: Windows 11

## 4. Comandos ejecutados

```bash
python src/00_verificar_entorno.py
python src/01_explorar_datos.py
python src/02_reporte_rural_CON_ERRORES.py
python src/03_pruebas_reporte.py
```

## 5. Resultado obtenido

El script `src/02_reporte_rural_CON_ERRORES.py` genero el archivo de salida:

- `output/reporte_rural.txt`

El reporte contiene un resumen por producto con `cantidad_total`, `ingreso_total estimado` y `registros`, la finca con mayor ingreso estimado y el numero de registros invalidos detectados.

## 6. Errores corregidos

Principales correcciones aplicadas en `src/02_reporte_rural_CON_ERRORES.py` (por bloques):

- Bloque 1 (rutas): corregida ruta del CSV a `data/produccion_rural.csv` y ruta de salida a `output/reporte_rural.txt`.
- Bloque 2 (lectura): `leer_csv()` retornaba una variable inexistente; se retornó la lista real de filas.
- Bloque 3 (conversion numérica): la conversión ahora maneja vacíos/textos invalidos devolviendo `None`.
- Bloque 4 (fechas): se ajustó el formato a `YYYY-MM-DD`.
- Bloque 5 (limpieza): validaciones para descartar registros con cantidad/precio no convertibles, finca vacía, fecha inválida y cantidades negativas.
- Bloque 6 (analisis por producto): acumulación correcta (se suma a `cantidad_total`/`ingreso_total`).
- Bloque 7 (finca mayor ingreso): se corrigio el retorno de la variable y se devolvio la finca correcta.
- Bloque 9 (funcion principal): se corrigió el nombre de la funcion llamada desde `main()`.

## 7. Comparacion tecnica del entorno

Se completa en `docs/matriz_comparacion_entorno.md`.

## 8. Conclusion

Se recomienda el entorno para proyectos similares de procesamiento de datos en CSV con depuracion incremental. Resulto eficaz por su estructura clara de carpetas, la capacidad de ejecutar scripts en terminal y el uso de errores tipicos de Python (FileNotFoundError/NameError/KeyError/ValueError/TypeError) para guiar correcciones hasta superar pruebas automatizadas.

