import csv
import requests
from bs4 import BeautifulSoup

def get_web_fragment(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    start_tag = soup.find(string=lambda text: 'Description-Begin -->' in text)
    end_tag = soup.find(string=lambda text: 'Description-End -->' in text)
    fragment = ''
    for elem in start_tag.parent.next_elements:
        if elem == end_tag:
            break
        fragment += str(elem)
    return fragment

def main():
    with open('links.csv', 'r') as file:
        reader = csv.reader(file)
        with open('output.csv', 'w', newline='') as output_file:
            writer = csv.writer(output_file)
            for row in reader:
                url = row[2]  # Enlace en la columna 3
                fragment = get_web_fragment(url)
                writer.writerow([url, fragment])

if __name__ == "__main__":
    main()