# SCRIPTS FOLDER

**Word Document Translator**
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

