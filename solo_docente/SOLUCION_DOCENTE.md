# Solucion docente

Esta carpeta contiene una solucion de referencia. Recomendacion: antes de compartir el ZIP con los estudiantes, retire la carpeta `solo_docente/` si no desea que tengan acceso a la respuesta.

## Errores principales incluidos en el script del estudiante

1. Ruta incorrecta del CSV: usa `produccion.csv` en lugar de `produccion_rural.csv`.
2. Carpeta de salida incorrecta: usa `outputs/` en lugar de `output/`.
3. Variable de retorno incorrecta en `leer_csv`: retorna `registros`, pero la variable real es `filas`.
4. Conversion numerica sin manejo de valores vacios o textos invalidos.
5. Formato de fecha incorrecto: usa `%d/%m/%Y` cuando el CSV usa `%Y-%m-%d`.
6. Nombre de columna incorrecto: `cantida` en lugar de `cantidad`.
7. Regla de limpieza incorrecta: cantidades negativas pasan como validas.
8. Acumulacion incorrecta: `cantidad_total = cantidad` deberia ser `+= cantidad`.
9. Variable de retorno inexistente: `finca_mas_alta`.
10. Funcion llamada con nombre incorrecto: `analizar_productos` en lugar de `analizar_por_producto`.
11. Falta crear la carpeta de salida antes de escribir el reporte.

## Prueba recomendada para validar

Copie el contenido de `solo_docente/02_reporte_rural_SOLUCION.py` dentro de `src/02_reporte_rural_CON_ERRORES.py` y ejecute:

```bash
python src/03_pruebas_reporte.py
```

Debe finalizar con el mensaje de pruebas superadas.
