# Guia del estudiante
## Semana 13: Artefacto del entorno con correccion de errores

### 1. Proposito de la actividad

En esta actividad vas a construir un artefacto tecnico ejecutable. No se trata solo de escribir codigo, sino de demostrar que puedes usar un entorno de programacion de forma profesional: abrir un proyecto, revisar archivos, ejecutar comandos, interpretar errores, corregirlos, generar un resultado y documentar evidencias.

La actividad evalua tres criterios tecnicos principales:

- **Funcionalidad:** que el entorno permita editar codigo, ejecutar scripts, revisar errores, leer archivos CSV y generar reportes.
- **Compatibilidad:** que la solucion funcione en equipos reales usando Python estandar y archivos comunes como CSV y TXT.
- **Costo:** que la solucion pueda realizarse con herramientas gratuitas o de bajo costo, sin depender de software pago.

### 2. Contexto del problema

Una comunidad rural tiene miles de registros de produccion en un archivo CSV. La informacion incluye finca, producto, cantidad, precio unitario, fecha y observaciones. El sistema debe generar un reporte automatico para ayudar a tomar decisiones.

Sin embargo, el script principal tiene varios errores. Tu trabajo consiste en corregirlos y demostrar que la mini-solucion funciona.

### 3. Que debes hacer

1. Descomprime el ZIP.
2. Abre la carpeta completa en Visual Studio Code.
3. Ejecuta el script de verificacion del entorno.
4. Explora el CSV para entender sus columnas.
5. Ejecuta el script con errores.
6. Corrige los errores uno por uno.
7. Registra cada error en la bitacora.
8. Ejecuta las pruebas finales.
9. Genera el reporte en `output/reporte_rural.txt`.
10. Entrega el proyecto corregido en un nuevo ZIP.

### 4. Comandos iniciales

Abre la terminal integrada de VS Code y ejecuta:

```bash
python src/00_verificar_entorno.py
```

Luego ejecuta:

```bash
python src/01_explorar_datos.py
```

Despues ejecuta el archivo con errores:

```bash
python src/02_reporte_rural_CON_ERRORES.py
```

Es normal que falle. Ese es el punto de la actividad.

### 5. Como corregir los errores

No intentes corregir todo al tiempo. Trabaja asi:

1. Ejecuta el script.
2. Lee el mensaje de error completo.
3. Identifica el archivo y la linea donde ocurre.
4. Corrige solo ese error.
5. Guarda el archivo.
6. Ejecuta de nuevo.
7. Registra el error y la solucion en la bitacora.

### 6. Prueba final

Cuando el script parezca funcionar, ejecuta:

```bash
python src/03_pruebas_reporte.py
```

Si las pruebas se superan, el artefacto esta listo.

### 7. Entregable

Debes entregar un ZIP con:

- proyecto corregido;
- archivo `output/reporte_rural.txt` generado;
- bitacora de errores diligenciada;
- informe final;
- README actualizado si hiciste cambios;
- evidencias de pruebas.

### 8. Recomendacion tecnica

Un buen tecnico no solo corrige errores: tambien explica que paso, por que paso, como lo soluciono y como comprobo que la solucion funciona.
