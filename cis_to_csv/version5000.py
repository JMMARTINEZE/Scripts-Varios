import csv
import docx

# Lista de palabras como cabecera
header = [
    'Title',
    'Profile Applicability',
    'Description',
    'Rationale',
    'Impact',
    'Audit',
    'Remediation',
    'Default Value'
]

# Crear el archivo CSV
with open('CIS_FIREFOX.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)

# Abrir el documento Word
doc = docx.Document('CIS_FIREFOX.docx')

# Leer los títulos de nivel 1
titulos = [p.text for p in doc.paragraphs if p.style.name.startswith('Heading 1')]

# Abrir el archivo CSV y rellenar la columna "Title"
with open('CIS_FIREFOX.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    for titulo in titulos:
        writer.writerow([titulo, '', '', '', '', '', '', ''])