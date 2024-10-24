import pandas as pd
from bs4 import BeautifulSoup
import chardet
import sys


def detect_encoding(file_path):
    with open(file_path, 'rb') as file:
        raw_data = file.read(1024)
    result = chardet.detect(raw_data)
    return result['encoding']


def main(html_file):
    encoding = detect_encoding(html_file)
    print(f"Codificación detectada: {encoding}")

    with open(html_file, 'r', encoding=encoding) as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')

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
    df.to_excel('html_to_excel/fields.xlsx', index=False)
    df.to_csv('html_to_excel/fields.csv', index=False)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python fields_html_to_excel.py <html_file>")
        sys.exit(1)

    html_file = sys.argv[1]
    main(html_file)