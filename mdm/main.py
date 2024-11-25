import requests
from bs4 import BeautifulSoup
import openpyxl

# URL de la página web
url = "https://learn.microsoft.com/en-us/mem/intune/protect/security-baseline-settings-mdm-all?pivots=mdm-23h2"

# Hacer la solicitud a la página web
response = requests.get(url)
response.raise_for_status()  # Asegura que la solicitud fue exitosa

# Parsear el contenido HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Crear un libro de Excel
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Datos Extraídos"
ws.append(["Configuración", "Valor Predeterminado", "Enlace"])  # Encabezados

# Extraer datos
for li in soup.find_all('li'):
    # Buscar etiquetas relevantes dentro del elemento <li>
    strong = li.find('strong')
    em = li.find('em')
    a = li.find('a')

    # Obtener valores o asignar texto vacío si no existen
    configuracion = strong.get_text(strip=True) if strong else "Sin configuración"
    valor_predeterminado = em.get_text(strip=True) if em else "Sin valor predeterminado"
    enlace = a['href'] if a else "Sin enlace"

    # Agregar fila al Excel
    ws.append([configuracion, valor_predeterminado, enlace])

# Guardar el archivo Excel
archivo_excel = "datos_extraidos.xlsx"
wb.save(archivo_excel)
print(f"Datos guardados en {archivo_excel}")
