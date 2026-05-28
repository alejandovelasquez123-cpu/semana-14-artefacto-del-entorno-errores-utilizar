"""
01_explorar_datos.py

Objetivo del script:
Explorar el archivo CSV principal sin usar librerias externas. Este script permite observar encabezados, cantidad de registros y primeras filas.

Este archivo NO tiene errores intencionales. Sirve como ejemplo de lectura correcta de archivos CSV.
"""
from pathlib import Path
import csv

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "produccion_rural.csv"

print("EXPLORACION DEL ARCHIVO CSV")
print("-" * 40)
print("Archivo:", DATA_FILE)

with DATA_FILE.open("r", encoding="utf-8", newline="") as archivo:
    lector = csv.DictReader(archivo)
    filas = list(lector)

print("Cantidad de registros:", len(filas))
print("Columnas encontradas:", lector.fieldnames)

print("\nPrimeras 5 filas:")
for fila in filas[:5]:
    print(fila)

print("\nObservacion tecnica:")
print("Antes de analizar un CSV, siempre revisa columnas, cantidad de filas y ejemplos reales de registros.")
