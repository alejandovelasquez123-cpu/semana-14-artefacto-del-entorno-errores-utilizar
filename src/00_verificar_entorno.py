"""
00_verificar_entorno.py

Objetivo del script:
Verificar que el estudiante puede ejecutar Python desde la terminal integrada de VS Code y que la estructura minima del proyecto existe.

Este archivo NO tiene errores intencionales. Sirve como primera prueba del entorno.
"""
from pathlib import Path
import sys

BASE_DIR = Path(__file__).resolve().parent.parent
CARPETAS_ESPERADAS = ["data", "src", "output", "docs", "evidencias"]

print("VERIFICACION DEL ENTORNO")
print("-" * 35)
print("Version de Python:", sys.version.split()[0])
print("Carpeta base del proyecto:", BASE_DIR)

print("\nRevision de carpetas:")
for carpeta in CARPETAS_ESPERADAS:
    ruta = BASE_DIR / carpeta
    if ruta.exists():
        print(f"OK  - existe la carpeta {carpeta}")
    else:
        print(f"ERROR - falta la carpeta {carpeta}")

archivo_datos = BASE_DIR / "data" / "produccion_rural.csv"
if archivo_datos.exists():
    print("\nOK - archivo de datos encontrado:", archivo_datos.name)
else:
    print("\nERROR - no se encontro el archivo produccion_rural.csv")

print("\nSi ves este mensaje, tu entorno puede ejecutar Python correctamente.")
