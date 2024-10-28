# SCRIPTS FOLDER

**Word Document Translator**
==========================

**Overview**
------------

Este proyecto es un script de Python que traduce texto en un documento de Word utilizando una clase `Translator` personalizada. Lee un archivo CSV, traduce el texto y guarda el documento resultante preservando la plantilla original.

**Requisitos**
---------------

* Python 3.x
* Bibliotecas requeridas (ver `requirements.txt`)
* Archivo CSV con texto a traducir (e.g. `combined_output.csv`)
* Plantilla de documento de Word (e.g. `template.docx`)

**Uso**
-----

1. Instala las bibliotecas requeridas ejecutando `pip install -r requirements.txt`
2. Crea un archivo CSV con el texto a traducir (e.g. `combined_output.csv`)
3. Crea una plantilla de documento de Word (e.g. `template.docx`)
4. Ejecuta el script utilizando `python main.py`
5. El documento traducido se guardará como `traducciones_respetando_template.docx`

**Estructura del Código**
------------------------

El código se organiza en los siguientes archivos:

* `main.py`: El script principal que procesa el documento de Word y traduce el texto.
* `utils/`: Carpeta con utilidades y clases auxiliares.
	+ `translator.py`: Clase `Translator` personalizada que traduce texto utilizando una API de terceros.
	+ `document_processor.py`: Clase que procesa el documento de Word y aplica la traducción.
* `csv_processors/`: Carpeta con scripts que procesan archivos CSV.
	+ `combine_csv.py`: Script que combina archivos CSV.
	+ `fields_html_to_csv.py`: Script que extrae campos de un archivo HTML y los convierte en un archivo CSV.
	+ `html_to_csv.py`: Script que extrae texto de un archivo HTML y lo convierte en un archivo CSV.
	+ `titles_html_to_csv.py`: Script que extrae títulos de un archivo HTML y los convierte en un archivo CSV.

Project
|___ html
|  |___ demo.html
|
|___ options
|  |___ config.json
|  |___ template.docx
|
|___ utils
|  |___ translator.py
|  |___ document_processor.py
|
|___ csv_processors
|  |___ __init__.py
|  |___ combine_csv.py
|  |___ fields_html_to_csv.py
|  |___ html_to_csv.py
|  |___ titles_html_to_csv.py
|
|___ main.py
|
|___ README.md
|___ requirements.txt

**Notas**
-----

* Este script asume que el archivo CSV tiene una estructura específica y que el texto a traducir está en una columna específica.
* El script utiliza la biblioteca `docx` para leer y escribir documentos de Word, y la biblioteca `chardet` para detectar la codificación del archivo CSV.
* La clase `Translator` es personalizada y debe ser implementada por el usuario.

**Posibles Fallos**
-------------------

* Si el archivo CSV no tiene la estructura esperada, el script puede fallar.
* Si la plantilla de documento de Word no es válida, el script puede fallar.
* Si la API de traducción de terceros no está disponible, el script puede fallar.


