import pandas as pd
from bs4 import BeautifulSoup
import chardet
import sys
import json

def detect_encoding(file_path):
    """
    Detects the encoding of a file.

    Args:
        file_path (str): The path to the file to detect the encoding of.

    Returns:
        str: The detected encoding of the file.
    """
    
    with open(file_path, 'rb') as file:
        raw_data = file.read(1024)
    result = chardet.detect(raw_data)
    return result['encoding']

def load_config(config_file):
    """
    Loads the configuration from a JSON file.

    Args:
        config_file (str): The path to the JSON file containing the configuration.

    Returns:
        dict: The loaded configuration.
    """
    with open(config_file, 'r') as f:
        config = json.load(f)
    return config

def main(html_file, config_file):
    """
    Processes an HTML file to extract specified fields and saves the data to Excel and CSV files.

    Args:
        html_file (str): The path to the HTML file to be processed.
        config_file (str): The path to the JSON configuration file specifying fields to extract.

    The function detects the encoding of the HTML file, parses it using BeautifulSoup,
    and extracts the values of fields defined in the configuration file. The extracted
    data is organized into a list of problems and saved as both an Excel and a CSV file.
    """
    encoding = detect_encoding(html_file)
    print(f"Codificación detectada: {encoding}")

    with open(html_file, 'r', encoding=encoding) as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')

    config = load_config(config_file)
    fields_to_extract = config['fields']

    problems = []
    field_tags = soup.find_all('b')
    field_dict = {}
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
                        field_dict[len(problems)] = current_line
                        problems.append(current_line)
                        current_line = {}
                    current_line[field_name] = field_value
                else:
                    current_line[field_name] = field_value

    if current_line:
        field_dict[len(problems)] = current_line
        problems.append(current_line)

    df = pd.DataFrame(problems)
    # df.to_excel('../outputs/fields.xlsx', index=False) Change it if you want an excel file
    df.to_csv('../outputs/fields.csv', index=False)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python fields_html_to_csv.py <html_file> <config_file>")
        sys.exit(1)

    html_file = sys.argv[1]
    config_file = sys.argv[2]
    main(html_file, config_file)