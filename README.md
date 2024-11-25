# SCRIPTS FOLDER

## **Word Document Translator**
==========================

**Overview**
------------

This project is a Python script that translates text in a Word document using a custom `Translator` class. It reads a CSV file, translates the text, and saves the resulting document while preserving the original template.

**Requirements**
---------------

* Python 3.x
* `docx` library (`pip install docx`)
* `chardet` library (`pip install chardet`)
* `translator` library (custom implementation, see below)

**Usage**
-----

1. Install the required libraries by running `pip install -r requirements.txt`
2. Create a CSV file containing the text to be translated (e.g. `combined_output.csv`)
3. Create a Word document template (e.g. `template.docx`)
4. Run the script using `python word_processor.py`
5. The translated document will be saved as `traducciones_respetando_template.docx`

**Translator Class**
-----------------

The `Translator` class is a custom implementation that translates text using a third-party API. You will need to implement this class yourself or use an existing translation library.

**Code Structure**
-----------------

The code is organized into the following files:

* `word_processor.py`: The main script that processes the Word document and translates the text.
* `translator.py`: The custom `Translator` class implementation (not included in this repository).

**Notes**
-----

* This script assumes that the CSV file has a specific structure and that the text to be translated is in a specific column.
* The script uses the `docx` library to read and write Word documents, and the `chardet` library to detect the encoding of the CSV file.
* The `Translator` class is not included in this repository and must be implemented separately.


## **Excel Document Translator**
================================

**Descripción**
---------------

Esta aplicación es un traductor de Excel que utiliza la API de Google Translate para traducir texto en archivos de Excel. Permite traducir texto en celdas individuales o en toda la hoja de cálculo.

**Funcionalidades**
-------------------

* Traduce texto en celdas individuales o en toda la hoja de cálculo
* Utiliza la API de Google Translate para obtener traducciones precisas
* Compatible con archivos de Excel (.xlsx, .xls)

**Requisitos**
--------------

* Python 3.x
* Biblioteca `pandas` para leer y escribir archivos de Excel
* Biblioteca `googletrans` para utilizar la API de Google Translate
* Biblioteca `tqdm` para tener un contador de gestión

**Uso**
-----

1. Instala las bibliotecas requeridas: `pip install pandas googletrans`
2. Descarga el archivo de Excel que deseas traducir
3. Ejecuta el script: `python traductor_excel.py`
4. Selecciona el archivo de Excel que deseas traducir y el idioma de destino
5. La aplicación traducirá el texto en el archivo de Excel y lo guardará en un nuevo archivo

**Ejemplo**
---------

Supongamos que tienes un archivo de Excel llamado `documento.xlsx` con el siguiente contenido:

| Columna A | Columna B |
| --- | --- |
| Hola | Mundo |

Puedes ejecutar el script y seleccionar el archivo `documento.xlsx` y el idioma de destino `inglés`. La aplicación traducirá el texto en el archivo de Excel y lo guardará en un nuevo archivo llamado `documento_traducido.xlsx` con el siguiente contenido:

| Columna A | Columna B |
| --- | --- |
| Hello | World |

**Licencia**
------------

Este proyecto está bajo la licencia MIT. Puedes utilizar, modificar y distribuir el código libremente.