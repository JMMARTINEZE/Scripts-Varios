import pandas as pd
from bs4 import BeautifulSoup
import chardet

def detect_encoding(file_path):
    with open(file_path, 'rb') as file:
        raw_data = file.read(1024)
    result = chardet.detect(raw_data)
    return result['encoding']

# Ruta al archivo HTML
html_file = r"html_to_excel\demo.html"

# Detectar la codificación del archivo
encoding = detect_encoding(html_file)
print(f"Codificación detectada: {encoding}")

# Leer el archivo HTML con la codificación detectada
with open(html_file, 'r', encoding=encoding) as file:
    html_content = file.read()

# Usar BeautifulSoup para parsear el HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Inicializar lista para almacenar los problemas
problems = []

# Buscar todas las etiquetas que contengan los campos
field_tags = soup.find_all('b')

for field_tag in field_tags:
    field_name = field_tag.get_text(strip=True)
    if field_name.endswith(':'):
        field_name = field_name[:-1]  # Remove the colon
        value_tag = field_tag.find_next(['span', 'div', 'p'])
        if value_tag:
            field_value = value_tag.get_text(strip=True)
        else:
            field_value = ''
        problems.append({field_name: field_value})

# Crear DataFrame de pandas
df = pd.DataFrame(problems)

# Guardar en Excel
excel_path = r"html_to_excel\output_problemas.xlsx"
df.to_excel(excel_path, index=False)

# O guardar en CSV
csv_path = r"html_to_excel\output_problemas.csv"
df.to_csv(csv_path, index=False)