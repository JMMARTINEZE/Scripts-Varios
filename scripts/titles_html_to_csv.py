import pandas as pd
from bs4 import BeautifulSoup
import chardet
import sys


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


def main(html_file):
    """
    Extracts titles from an HTML file and saves them to a CSV file.

    Args:
        html_file (str): The path to the HTML file to extract titles from.

    The function detects the encoding of the HTML file, parses it using BeautifulSoup,
    and extracts the titles from the HTML. The extracted titles are organized into a
    list and saved as a CSV file named 'titles.csv' in the 'html_to_excel' folder.
    """
    encoding = detect_encoding(html_file)
    print(f"Codificación detectada: {encoding}")

    with open(html_file, 'r', encoding=encoding) as file:
        html_content = file.read()

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

    df = pd.DataFrame(titles, columns=['Title'])
    # df.to_excel('html_to_excel/titles.xlsx', index=False)  Change it if you want an excel file
    df.to_csv('html_to_excel/titles.csv', index=False, encoding='utf-8-sig')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python titles_html_to_csv.py <html_file>")
        sys.exit(1)

    html_file = sys.argv[1]
    main(html_file)