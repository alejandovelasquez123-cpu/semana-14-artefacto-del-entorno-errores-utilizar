# Artefacto del entorno - Semana 13
## Mini-solucion ejecutable con depuracion de errores

Este proyecto es una actividad practica para abrir en Visual Studio Code. El objetivo es que el estudiante configure un entorno de trabajo, ejecute scripts, analice archivos CSV grandes y corrija varios errores intencionales hasta obtener un producto ejecutable.

## Problema contextual

Una comunidad rural necesita revisar miles de registros de produccion relacionados con leche, maiz, yuca, huevos y queso. Los datos estan en archivos CSV y se requiere generar un reporte automatico que indique:

- total producido por producto;
- ingresos estimados por producto;
- finca con mayor ingreso;
- registros con problemas de calidad;
- archivo final de reporte dentro de la carpeta `output/`.

## Que debe entregar el estudiante

Debe entregar un link de git con el proyecto corregido, organizado y ejecutable. El proyecto debe incluir:

1. codigo corregido;
2. archivo de reporte generado;
3. bitacora de errores;
4. evidencias de pruebas;
5. README breve actualizado;
6. matriz de comparacion tecnica del entorno.

## Estructura del proyecto

```text
Artefacto_Entorno_Semana13_Errores/
|-- README.md
|-- requirements.txt
|-- data/
|   |-- produccion_rural.csv
|   |-- catalogo_productos.csv
|-- src/
|   |-- 00_verificar_entorno.py
|   |-- 01_explorar_datos.py
|   |-- 02_reporte_rural_CON_ERRORES.py
|   |-- 03_pruebas_reporte.py
|-- output/
|-- evidencias/
|   |-- plantilla_bitacora_errores.md
|   |-- plantilla_informe_final.md
|-- docs/
|   |-- GUIA_ESTUDIANTE.md
|   |-- explicacion_bloque_a_bloque.md
|   |-- pistas_depuracion.md
|   |-- matriz_comparacion_entorno.md
|   |-- rubrica.md
|   |-- checklist_entrega.md
|   |-- descripcion_moodle.md
|-- solo_docente/
|   |-- SOLUCION_DOCENTE.md
|   |-- 02_reporte_rural_SOLUCION.py
```

## Paso rapido para iniciar

Abre una terminal en VS Code y ejecuta:

```bash
python src/00_verificar_entorno.py
python src/01_explorar_datos.py
python src/02_reporte_rural_CON_ERRORES.py
```

El tercer comando debe fallar al inicio. Esa falla es intencional. El reto consiste en corregir el archivo `src/02_reporte_rural_CON_ERRORES.py` hasta que funcione correctamente.

## Prueba final

Cuando creas que corregiste el proyecto, ejecuta:

```bash
python src/03_pruebas_reporte.py
```

Si la salida muestra que las pruebas fueron superadas, el artefacto esta listo para entregar.

## Criterios tecnicos trabajados

- Funcionalidad: el entorno permite abrir carpetas, editar codigo, ejecutar scripts, leer CSV y generar reportes.
- Compatibilidad: se usa Python estandar, sin dependencias externas obligatorias.
- Costo: se trabaja con VS Code y Python, herramientas gratuitas y adecuadas para equipos educativos.
- Evidencia de pruebas: el estudiante documenta comandos, errores y resultados.
- Organizacion: el proyecto usa carpetas separadas para datos, codigo, salidas, documentos y evidencias.
