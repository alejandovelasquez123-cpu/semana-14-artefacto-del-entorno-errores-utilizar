"""
03_pruebas_reporte.py

Objetivo del script:
Verificar si el artefacto corregido funciona de manera minima.

IMPORTANTE:
Este archivo intenta importar funciones desde 02_reporte_rural_CON_ERRORES.py.
Si el archivo aun tiene errores de sintaxis, nombres de variables incorrectos o rutas malas, las pruebas fallaran.
"""
from pathlib import Path
import importlib.util
import sys

BASE_DIR = Path(__file__).resolve().parent.parent
SCRIPT_OBJETIVO = BASE_DIR / "src" / "02_reporte_rural_CON_ERRORES.py"
DATA_FILE = BASE_DIR / "data" / "produccion_rural.csv"
OUTPUT_FILE = BASE_DIR / "output" / "reporte_rural.txt"


def cargar_modulo_desde_archivo(ruta):
    spec = importlib.util.spec_from_file_location("reporte_rural_estudiante", ruta)
    modulo = importlib.util.module_from_spec(spec)
    sys.modules["reporte_rural_estudiante"] = modulo
    spec.loader.exec_module(modulo)
    return modulo


def verificar(condicion, mensaje_ok, mensaje_error):
    if condicion:
        print("OK -", mensaje_ok)
    else:
        print("ERROR -", mensaje_error)
        raise AssertionError(mensaje_error)


print("PRUEBAS DEL ARTEFACTO")
print("-" * 35)

modulo = cargar_modulo_desde_archivo(SCRIPT_OBJETIVO)

registros = modulo.leer_csv(DATA_FILE)
verificar(len(registros) >= 8000, "se leyeron miles de registros", "no se leyeron los registros esperados")

validos, invalidos = modulo.limpiar_registros(registros)
verificar(len(validos) > 7000, "hay suficientes registros validos", "la limpieza dejo muy pocos registros validos")
verificar(len(invalidos) >= 4, "se detectaron registros invalidos", "no se detectaron los registros problematicos")

resumen = modulo.analizar_por_producto(validos)
productos_esperados = {"leche", "maiz", "yuca", "huevo", "queso"}
verificar(productos_esperados.issubset(set(resumen.keys())), "el resumen contiene los productos esperados", "faltan productos en el resumen")

for producto, datos in resumen.items():
    verificar(datos["cantidad_total"] > 0, f"{producto} tiene cantidad total positiva", f"{producto} no acumulo cantidad correctamente")
    verificar(datos["ingreso_total"] > 0, f"{producto} tiene ingreso total positivo", f"{producto} no calculo ingreso correctamente")

finca_mayor, ingreso_mayor = modulo.calcular_finca_mayor_ingreso(validos)
verificar(isinstance(finca_mayor, str) and finca_mayor.strip() != "", "se identifico finca con mayor ingreso", "no se identifico finca mayor")
verificar(ingreso_mayor > 0, "el ingreso mayor es positivo", "el ingreso mayor no es valido")

ruta_reporte = modulo.generar_reporte(resumen, invalidos, finca_mayor, ingreso_mayor)
verificar(ruta_reporte.exists(), "el archivo de reporte fue creado", "no se creo el archivo de reporte")
verificar(ruta_reporte == OUTPUT_FILE, "el reporte se genero en la carpeta output", "el reporte no esta en la ruta esperada output/reporte_rural.txt")

contenido = ruta_reporte.read_text(encoding="utf-8")
verificar("REPORTE RURAL AUTOMATICO" in contenido, "el reporte tiene titulo", "el reporte no tiene el titulo esperado")
verificar("Registros invalidos detectados" in contenido, "el reporte incluye registros invalidos", "el reporte no informa registros invalidos")

print("\nRESULTADO FINAL: pruebas superadas. El artefacto corregido esta listo para entregar.")
