# Pistas de depuracion

Usa este documento solo como ayuda. No contiene la solucion completa, pero si orienta el proceso.

## Pista 1: FileNotFoundError

Si Python dice que no encuentra un archivo, revisa:

- nombre exacto del archivo;
- carpeta donde esta guardado;
- si la ruta usa `data/` o una carpeta diferente.

## Pista 2: NameError

Un `NameError` indica que estas usando una variable o funcion que no existe con ese nombre.

Preguntas utiles:

- ¿La variable fue creada antes?
- ¿El nombre esta escrito igual?
- ¿Hay una diferencia entre singular y plural?

## Pista 3: KeyError

Un `KeyError` indica que intentas acceder a una columna que no existe en el CSV.

Solucion tecnica:

Ejecuta `01_explorar_datos.py` y revisa la lista de columnas reales.

## Pista 4: ValueError

Un `ValueError` puede aparecer cuando intentas convertir a numero un texto que no se puede convertir.

Ejemplos problematicos:

- campo vacio;
- texto `ERROR`;
- fecha imposible.

## Pista 5: Error logico

No todos los errores detienen el programa. Algunos producen resultados incorrectos.

Ejemplo:

```python
cantidad_total = cantidad
```

Eso reemplaza el valor anterior. Para acumular, se necesita:

```python
cantidad_total += cantidad
```

## Pista 6: Pruebas finales

Las pruebas del archivo `03_pruebas_reporte.py` te ayudan a detectar errores que tal vez no viste manualmente.
