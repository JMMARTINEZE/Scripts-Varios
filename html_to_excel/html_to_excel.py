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
fields = ['ID', 'Description', 'Remediation', 'PowerShell Script', 
          'Returned Value', 'Default Value', 'Expected Value', 
          'Impact', 'Likelihood', 'Priority', 'RiskRating', 'References']

problem_data = {}

for field in fields:
    field_tag = soup.find('b', string=f'{field}:')
    if field_tag:
        value_tag = field_tag.find_next(['span', 'div', 'p'])
        if value_tag:
            field_value = value_tag.get_text(strip=True)
        else:
            field_value = ''
        problem_data[field] = field_value

problems.append(problem_data)

# Crear DataFrame de pandas
df = pd.DataFrame(problems)

# Guardar en Excel
excel_path = r"html_to_excel\output_problemas.xlsx"
df.to_excel(excel_path, index=False)

# O guardar en CSV
csv_path = r"html_to_excel\output_problemas.csv"
df.to_csv(csv_path, index=False)