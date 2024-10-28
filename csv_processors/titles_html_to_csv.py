import pandas as pd
from bs4 import BeautifulSoup
import chardet
import sys
import os
import logging
from dotenv import load_dotenv

# Carga las variables de entorno desde el archivo .env
load_dotenv('../.env')

# Configuración de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

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

def process_html_file(html_file):
    """
    Extracts titles from an HTML file.

    Args:
        html_file (str): The path to the HTML file to extract titles from.
    """
    encoding = detect_encoding(html_file)
    logging.info(f"Codificación detectada: {encoding}")

    try:
        with open(html_file, 'r', encoding=encoding) as file:
            html_content = file.read()
    except Exception as e:
        logging.error(f"Error leyendo archivo HTML: {e}")
        return

    soup = BeautifulSoup(html_content, 'html.parser')

    header_bars = soup.find_all('div', class_='header-bar')

    titles = []

    for header_bar in header_bars:
        title_div = header_bar.find('div', class_='col-8')
        if title_div:
            title = title_div.find('h6')
            if title:
                title = title.get_text(strip=True)
                titles.append(title)

    return titles

def main():
    # Iterate over all HTML files in the input folder
    input_html_folder = os.getenv('INPUT_HTML_FOLDER')
    output_csv_file = os.getenv('OUTPUT_CSV_FILE')
    output_folder = os.getenv('OUTPUT_FOLDER')

    for file in os.listdir(input_html_folder):
        if file.endswith('.html'):
            html_file = os.path.join(input_html_folder, file)
            logging.info(f"Procesando archivo: {html_file}")
            titles = process_html_file(html_file)
            if titles:
                df = pd.DataFrame(titles, columns=['Title'])
                output_file = os.path.join(output_folder, f"{os.path.basename(html_file).replace('.html', '_titles.csv')}")
                try:
                    df.to_csv(output_file, index=False, encoding='utf-8-sig', mode='a', header=False)
                    logging.info(f"Archivo CSV generado correctamente: {output_file}")
                except Exception as e:
                    logging.error(f"Error escribiendo archivo CSV: {e}")

if __name__ == '__main__':
    main()