# Explicacion bloque a bloque del script principal

El archivo `src/02_reporte_rural_CON_ERRORES.py` esta organizado por bloques. Cada bloque cumple una responsabilidad tecnica especifica. Comprender estos bloques ayuda a depurar de manera ordenada.

## Bloque 1: Rutas del proyecto

Define donde esta la carpeta principal, donde esta el archivo de datos y donde se guardara el reporte.

Conceptos importantes:

- `Path(__file__)`: representa el archivo Python actual.
- `.resolve()`: convierte la ruta en una ruta absoluta.
- `.parent`: permite subir de carpeta.
- `BASE_DIR`: carpeta raiz del proyecto.

Errores posibles en este bloque:

- nombre de archivo incorrecto;
- carpeta de salida mal escrita;
- ruta relativa mal construida.

## Bloque 2: Lectura del CSV

Abre el archivo CSV y lo convierte en una lista de diccionarios. Cada fila queda como un diccionario donde las claves son los nombres de las columnas.

Ejemplo de registro:

```python
{
    'fecha': '2026-01-01',
    'finca': 'La Esperanza',
    'producto': 'leche',
    'cantidad': '25.5'
}
```

Error comun:

- retornar una variable que no existe.

## Bloque 3: Conversion numerica

Convierte valores leidos desde el CSV a numeros. En los CSV, casi todo entra como texto. Por eso `"25.5"` debe convertirse a `25.5`.

Error comun:

- intentar convertir valores vacios o textos como `ERROR` sin controlar excepciones.

## Bloque 4: Validacion de fechas

Comprueba si la fecha tiene un formato valido. En este proyecto el formato correcto es:

```text
YYYY-MM-DD
```

Ejemplo:

```text
2026-03-15
```

Error comun:

- usar un formato de fecha distinto al que realmente tiene el CSV.

## Bloque 5: Limpieza de datos

Separa registros validos e invalidos. Un registro debe considerarse invalido si:

- la cantidad esta vacia;
- la cantidad no es numerica;
- la cantidad es negativa;
- el precio no es numerico;
- la fecha es invalida;
- la finca esta vacia.

Este bloque es importante porque los datos reales casi nunca son perfectos.

## Bloque 6: Analisis por producto

Agrupa los registros por producto y calcula:

- cantidad total;
- ingreso total;
- cantidad de registros.

Error comun:

- reemplazar el acumulado en lugar de sumarlo.

Incorrecto:

```python
resumen[producto]["cantidad_total"] = cantidad
```

Correcto:

```python
resumen[producto]["cantidad_total"] += cantidad
```

## Bloque 7: Finca con mayor ingreso

Calcula el ingreso estimado por finca y selecciona la finca con el valor mayor.

Error comun:

- retornar una variable que nunca fue creada.

## Bloque 8: Generacion del reporte

Crea un archivo de texto con los resultados del analisis.

Antes de escribir un archivo, debes verificar que la carpeta exista:

```python
OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
```

## Bloque 9: Funcion principal

Coordina todo el proceso:

1. lee datos;
2. limpia registros;
3. analiza productos;
4. identifica finca con mayor ingreso;
5. genera reporte;
6. muestra resultados en terminal.

Error comun:

- llamar una funcion con un nombre que no existe.
