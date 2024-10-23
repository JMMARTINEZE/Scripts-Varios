import pandas as pd
from bs4 import BeautifulSoup
import chardet

# Función para detectar la codificación del archivo
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

# Buscar todas las etiquetas <h6> que actúan como títulos de los problemas
for h6_tag in soup.find_all('h6'):
    card_body = h6_tag.find_parent('div', class_='card-body')
    if card_body:
        fields = card_body.find_all(['b', 'span'], recursive=False)
        problem_data = {}
        for field in fields:
            if field.text.strip() in ['ID:', 'Description:', 'Remediation:', 'PowerShell Script:', 'Returned Value:', 'Default Value:', 'Expected Value:', 'Impact:', 'Likelihood:', 'Priority:', 'RiskRating:', 'References:']:
                next_sibling = field.find_next_sibling(string=True)
                value = next_sibling.strip() if next_sibling else ''
                problem_data[field.text.strip()] = value
        print(problem_data)

# Usar BeautifulSoup para parsear el HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Inicializar lista para almacenar los problemas
problems = []

# Buscar todas las etiquetas <h6> que actúan como títulos de los problemas
for h6_tag in soup.find_all('h6'):
    # Diccionario para almacenar la información de cada problema
    problem_data = {}
    
    # Título del problema (contenido del <h6>)
    problem_data['Title'] = h6_tag.get_text(strip=True)

    # Buscar el contenedor que tiene los detalles del problema
    card_body = h6_tag.find_parent('div', class_='card-body')
    
    # Si existe un card-body, proceder a buscar los detalles
    if card_body:
        # Buscar los campos específicos dentro del card-body
        for field in ['ID', 'Description', 'Remediation', 'PowerShell Script', 
                      'Returned Value', 'Default Value', 'Expected Value', 
                      'Impact', 'Likelihood', 'Priority', 'RiskRating', 'References']:
            # Intentar encontrar el campo correspondiente
            field_tag = card_body.find('b', string=f'{field}:')
            if field_tag:
                # Verificar que el siguiente hermano (next_sibling) no sea None y que sea texto
                next_sibling = field_tag.next_sibling
                if next_sibling and isinstance(next_sibling, str):
                    field_value = next_sibling.strip()
                else:
                    field_value = ''  # Si el campo no tiene contenido textual
                problem_data[field] = field_value
            else:
                problem_data[field] = ''  # Si el campo no está presente, dejarlo vacío
    
    # Agregar el problema a la listafor field in fields:
# Agregar el problema a la lista
for field in fields:
    if field.text.strip() in ['ID:', 'Description:', 'Remediation:', 'PowerShell Script:', 'Returned Value:', 'Default Value:', 'Expected Value:', 'Impact:', 'Likelihood:', 'Priority:', 'RiskRating:', 'References:']:
        next_sibling = field.find_next_sibling(string=True)  # Use 'string' instead of 'text'
        if next_sibling is not None:
            value = next_sibling.strip()
            print(f"{field.text.strip()}: {value}")
        else:
            print(f"{field.text.strip()}: No value found")

problems.append(problem_data)

# Crear DataFrame de pandas
df = pd.DataFrame(problems)

# Guardar en Excel
excel_path = "html_to_excel\output_problemas.xlsx"  # Cambia el nombre si es necesario
with pd.ExcelWriter(excel_path, engine='openpyxl') as writer:
    df.to_excel(writer, sheet_name='Auditoría Problemas', index=False)

print(f"Excel generado en {excel_path}")
