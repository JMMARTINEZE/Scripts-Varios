import os
import subprocess
import logging
import threading

logging.basicConfig(level=logging.INFO)


def extract_titles(html_filepath):
    try:
        subprocess.run(["python", "./csv_processors/titles_html_to_csv.py", html_filepath])
    except Exception as e:
        logging.error(f"Error extracting titles: {e}")


def extract_fields(html_filepath, config_filepath):
    try:
        subprocess.run(["python", "./csv_processors/fields_html_to_csv.py", html_filepath, config_filepath])
    except Exception as e:
        logging.error(f"Error extracting fields: {e}")


def combine_csv():
    try:
        subprocess.run(["python", "./csv_processors/combine_csv.py"])
    except Exception as e:
        logging.error(f"Error combining CSV: {e}")


def generate_word_document():
    try:
        subprocess.run(["python", "./utils/document_processor.py"])
    except Exception as e:
        logging.error(f"Error generating Word document: {e}")


def main():
    html_folder = "html"
    for file in os.listdir(html_folder):
        if file.endswith(".html"):
            html_filepath = os.path.join(html_folder, file)
            threading.Thread(target=extract_titles, args=(html_filepath,)).start()
            threading.Thread(target=extract_fields, args=(html_filepath, "options/fields_config.json",)).start()

    # Esperar a que se completen todas las tareas de extracción
    threading.Event().wait()

    # Ejecutar combine_csv.py
    combine_csv()

    # Esperar a que se complete combine_csv.py
    threading.Event().wait()

    # Ejecutar document_processor.py
    generate_word_document()


if __name__ == "__main__":
    main()