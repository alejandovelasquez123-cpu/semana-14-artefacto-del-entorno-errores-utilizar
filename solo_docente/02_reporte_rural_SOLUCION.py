"""
02_reporte_rural_SOLUCION.py

Solucion de referencia para docente.
No entregar esta carpeta a los estudiantes si se desea que resuelvan la actividad sin la respuesta.
"""
from pathlib import Path
import csv
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "produccion_rural.csv"
OUTPUT_FILE = BASE_DIR / "output" / "reporte_rural.txt"


def leer_csv(ruta_archivo):
    with ruta_archivo.open("r", encoding="utf-8", newline="") as archivo:
        lector = csv.DictReader(archivo)
        return list(lector)


def convertir_a_numero(valor):
    try:
        if valor is None or str(valor).strip() == "":
            return None
        return float(valor)
    except ValueError:
        return None


def fecha_valida(texto_fecha):
    try:
        datetime.strptime(texto_fecha, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def limpiar_registros(registros):
    validos = []
    invalidos = []

    for registro in registros:
        cantidad = convertir_a_numero(registro.get("cantidad"))
        precio = convertir_a_numero(registro.get("precio_unitario"))
        finca = registro.get("finca", "").strip()
        fecha = registro.get("fecha", "").strip()

        if cantidad is None or precio is None:
            invalidos.append(registro)
        elif cantidad < 0 or precio < 0:
            invalidos.append(registro)
        elif not fecha_valida(fecha):
            invalidos.append(registro)
        elif finca == "":
            invalidos.append(registro)
        else:
            registro["cantidad"] = cantidad
            registro["precio_unitario"] = precio
            registro["finca"] = finca
            validos.append(registro)

    return validos, invalidos


def analizar_por_producto(registros_validos):
    resumen = {}
    for registro in registros_validos:
        producto = registro["producto"]
        cantidad = registro["cantidad"]
        precio = registro["precio_unitario"]
        if producto not in resumen:
            resumen[producto] = {"cantidad_total": 0, "ingreso_total": 0, "registros": 0}
        resumen[producto]["cantidad_total"] += cantidad
        resumen[producto]["ingreso_total"] += cantidad * precio
        resumen[producto]["registros"] += 1
    return resumen


def calcular_finca_mayor_ingreso(registros_validos):
    ingresos = {}
    for registro in registros_validos:
        finca = registro["finca"]
        ingreso = registro["cantidad"] * registro["precio_unitario"]
        ingresos[finca] = ingresos.get(finca, 0) + ingreso
    finca_mayor = max(ingresos, key=ingresos.get)
    return finca_mayor, ingresos[finca_mayor]


def generar_reporte(resumen, invalidos, finca_mayor, ingreso_mayor):
    lineas = []
    lineas.append("REPORTE RURAL AUTOMATICO")
    lineas.append("=" * 35)
    lineas.append("")
    lineas.append("Resumen por producto:")
    for producto, datos in sorted(resumen.items()):
        lineas.append(f"- {producto}: cantidad total = {datos['cantidad_total']:.2f}, ingreso estimado = ${datos['ingreso_total']:.2f}, registros = {datos['registros']}")
    lineas.append("")
    lineas.append(f"Finca con mayor ingreso estimado: {finca_mayor} (${ingreso_mayor:.2f})")
    lineas.append(f"Registros invalidos detectados: {len(invalidos)}")

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_FILE.open("w", encoding="utf-8") as archivo:
        archivo.write("\n".join(lineas))
    return OUTPUT_FILE


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
