import pandas as pd
from bs4 import BeautifulSoup
import chardet

def detect_encoding(file_path):
    with open(file_path, 'rb') as file:
        raw_data = file.read(1024)
    result = chardet.detect(raw_data)
    return result['encoding']

def main():
    html_file = r"html_to_excel\demo.html"
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
    df.to_excel('html_to_excel/titles.xlsx', index=False)

if __name__ == '__main__':
    main()