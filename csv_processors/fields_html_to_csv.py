import pandas as pd
from bs4 import BeautifulSoup
import chardet
import sys
import json
import logging
import os
from dotenv import load_dotenv

# Carga las variables de entorno desde el archivo .env
load_dotenv('../.env')

# Configuración de logging
logging.basicConfig(level=logging.INFO)

def detect_encoding(file_path):
    """
    Detects the encoding of a file.

    Args:
        file_path (str): The path to the file to detect the encoding of.

    Returns:
        str: The detected encoding of the file.
    """
    try:
        with open(file_path, 'rb') as file:
            raw_data = file.read(1024)
        result = chardet.detect(raw_data)
        return result['encoding']
    except Exception as e:
        logging.error(f"Error detecting encoding: {e}")
        return None

def load_config(config_file):
    """
    Loads the configuration from a JSON file.

    Args:
        config_file (str): The path to the JSON file containing the configuration.

    Returns:
        dict: The loaded configuration.
    """
    try:
        with open(config_file, 'r') as f:
            config = json.load(f)
        return config
    except Exception as e:
        logging.error(f"Error loading configuration: {e}")
        return None

def process_html_file(html_file, config_file, output_folder):
    try:
        encoding = detect_encoding(html_file)
        if encoding is None:
            logging.error("Error detecting encoding")
            return
        logging.info(f"Detected encoding: {encoding}")

        with open(html_file, 'r', encoding=encoding) as file:
            html_content = file.read()

        soup = BeautifulSoup(html_content, 'html.parser')

        config = load_config(config_file)
        if config is None:
            logging.error("Error loading configuration")
            return
        fields_to_extract = config['fields']

        problems = []
        field_tags = soup.find_all('b')
        current_line = {}

        for field_tag in field_tags:
            field_name = field_tag.get_text(strip=True)
            if field_name.endswith(':'):
                field_name = field_name[:-1]  # Remove the colon
                value_tag = field_tag.find_next(['span', 'div', 'p'])
                if value_tag:
                    field_value = value_tag.get_text(strip=True)
                else:
                    field_value = ''

                if field_name in fields_to_extract:
                    if field_name == 'Description':
                        if current_line:
                            problems.append(current_line)
                            current_line = {}
                        current_line[field_name] = field_value
                    else:
                        current_line[field_name] = field_value

        if current_line:
            problems.append(current_line)

        df = pd.DataFrame(problems)
        output_file = os.path.join(output_folder, os.path.basename(html_file).replace('.html', '_fields.csv'))
        df.to_csv(output_file, index=False)
        logging.info(f"CSV file generated successfully: {output_file}")
    except Exception as e:
        logging.error(f"Error processing HTML file: {e}")

def main(config_file, output_folder):
    html_folder = os.getenv('INPUT_HTML_FOLDER')
    files = os.listdir(html_folder)
    html_files = [file for file in files if file.endswith('.html')]

    for file in html_files:
        html_file = os.path.join(html_folder, file)
        process_html_file(html_file, config_file, output_folder)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python fields_html_to_csv.py <config_file>")
        sys.exit(1)

    config_file = sys.argv[1]
    output_folder = os.getenv('OUTPUT_FOLDER')
    main(config_file, output_folder)