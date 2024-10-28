import os
import subprocess
import logging

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
    html_filepath = input("Enter the path to the original HTML file: ")
    extract_titles(html_filepath)
    config_filepath = "options/fields_config.json"
    extract_fields(html_filepath, config_filepath)
    combine_csv()
    generate_word_document()

if __name__ == "__main__":
    main()