"""
02_reporte_rural_CON_ERRORES.py

RETO DEL ESTUDIANTE
Este archivo contiene varios errores intencionales. Tu mision es corregirlos para que el programa pueda:

1. leer el archivo data/produccion_rural.csv;
2. limpiar registros con datos invalidos;
3. calcular total producido por producto;
4. calcular ingresos estimados por producto;
5. detectar registros con errores;
6. generar el archivo output/reporte_rural.txt;
7. superar las pruebas del archivo src/03_pruebas_reporte.py.

No borres la estructura completa. Corrige bloque por bloque.
Documenta cada error en evidencias/plantilla_bitacora_errores.md.
"""

from pathlib import Path
import csv
from datetime import datetime

# ==========================================================
# BLOQUE 1: RUTAS DEL PROYECTO
# Error intencional 1: revisa si el nombre del archivo CSV es correcto.
# ==========================================================
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "produccion_rural.csv"
OUTPUT_FILE = BASE_DIR / "output" / "reporte_rural.txt"


# ==========================================================
# BLOQUE 2: LECTURA DEL CSV
# Error intencional 2: revisa el nombre de la variable que se retorna.
# ==========================================================
def leer_csv(ruta_archivo):
    """Lee un archivo CSV y retorna una lista de diccionarios."""
    with ruta_archivo.open("r", encoding="utf-8", newline="") as archivo:
        lector = csv.DictReader(archivo)
        filas = list(lector)
    return filas


# ==========================================================
# BLOQUE 3: CONVERSION NUMERICA
# Error intencional 3: la funcion debe manejar valores vacios o textos invalidos.
# ==========================================================
def convertir_a_numero(valor):
    """Convierte un valor a numero decimal. Retorna None si no puede convertirse."""
    try:
        if valor is None:
            return None
        valor = str(valor).strip()
        if valor == "":
            return None
        return float(valor)
    except (ValueError, TypeError):
        return None


# ==========================================================
# BLOQUE 4: VALIDACION DE FECHAS
# Error intencional 4: el formato de fecha usado no coincide con el CSV.
# ==========================================================
def fecha_valida(texto_fecha):
    """Retorna True si la fecha es valida y False si no lo es."""
    try:
        # El CSV usa formato YYYY-MM-DD
        datetime.strptime(texto_fecha, "%Y-%m-%d")
        return True
    except ValueError:
        return False


# ==========================================================
# BLOQUE 5: LIMPIEZA DE DATOS
# Errores intencionales 5 y 6: revisa nombres de columnas y reglas de limpieza.
# ==========================================================
def limpiar_registros(registros):
    """Separa registros validos e invalidos."""
    validos = []
    invalidos = []

    for registro in registros:
        cantidad = convertir_a_numero(registro["cantidad"])
        precio = convertir_a_numero(registro["precio_unitario"])

        # Validaciones: cantidad y precio deben ser números convertibles
        if cantidad is None or precio is None:
            invalidos.append(registro)
        elif cantidad < 0:
            invalidos.append(registro)
        elif not fecha_valida(registro["fecha"]):
            invalidos.append(registro)
        elif registro["finca"].strip() == "":
            invalidos.append(registro)
        else:
            registro["cantidad"] = cantidad
            registro["precio_unitario"] = precio
            validos.append(registro)

    return validos, invalidos


# ==========================================================
# BLOQUE 6: ANALISIS DE PRODUCTOS
# Error intencional 7: revisa si se esta acumulando correctamente.
# ==========================================================
def analizar_por_producto(registros_validos):
    """Calcula total producido e ingreso estimado por producto."""
    resumen = {}

    for registro in registros_validos:
        producto = registro["producto"]
        cantidad = registro["cantidad"]
        precio = registro["precio_unitario"]

        if producto not in resumen:
            resumen[producto] = {"cantidad_total": 0, "ingreso_total": 0, "registros": 0}

        resumen[producto]["cantidad_total"] = cantidad
        resumen[producto]["ingreso_total"] += cantidad * precio
        resumen[producto]["registros"] += 1

    return resumen


# ==========================================================
# BLOQUE 7: FINCA CON MAYOR INGRESO
# Error intencional 8: revisa el nombre de la variable usada en el return.
# ==========================================================
def calcular_finca_mayor_ingreso(registros_validos):
    """Identifica la finca con mayor ingreso estimado."""
    ingresos = {}

    for registro in registros_validos:
        finca = registro["finca"]
        ingreso = registro["cantidad"] * registro["precio_unitario"]
        ingresos[finca] = ingresos.get(finca, 0) + ingreso

    finca_mayor = max(ingresos, key=ingresos.get)
    return finca_mayor, ingresos[finca_mayor]


# ==========================================================
# BLOQUE 8: GENERACION DEL REPORTE
# Error intencional 9: revisa si la carpeta de salida existe antes de escribir.
# ==========================================================
def generar_reporte(resumen, invalidos, finca_mayor, ingreso_mayor):
    """Genera un archivo de reporte en texto plano."""
    lineas = []
    lineas.append("REPORTE RURAL AUTOMATICO")
    lineas.append("=" * 35)
    lineas.append("")
    lineas.append("Resumen por producto:")

    for producto, datos in resumen.items():
        lineas.append(f"- {producto}: cantidad total = {datos['cantidad_total']:.2f}, ingreso estimado = ${datos['ingreso_total']:.2f}, registros = {datos['registros']}")

    lineas.append("")
    lineas.append(f"Finca con mayor ingreso estimado: {finca_mayor} (${ingreso_mayor:.2f})")
    lineas.append(f"Registros invalidos detectados: {len(invalidos)}")

    with OUTPUT_FILE.open("w", encoding="utf-8") as archivo:
        archivo.write("\n".join(lineas))

    return OUTPUT_FILE


# ==========================================================
# BLOQUE 9: FUNCION PRINCIPAL
# Error intencional 10: revisa el orden y los nombres de las funciones llamadas.
# ==========================================================
def main():
    print("Generando reporte rural...")
    registros = leer_csv(DATA_FILE)
    validos, invalidos = limpiar_registros(registros)
    resumen = analizar_por_producto(validos)
    finca_mayor, ingreso_mayor = calcular_finca_mayor_ingreso(validos)
    ruta_reporte = generar_reporte(resumen, invalidos, finca_mayor, ingreso_mayor)

    print("Reporte generado correctamente en:", ruta_reporte)
    print("Registros validos:", len(validos))
    print("Registros invalidos:", len(invalidos))


if __name__ == "__main__":
    main()
