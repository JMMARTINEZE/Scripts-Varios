import os
import PyPDF2
import pdfkit

# Directorio donde se encuentran los PDF
directorio = 'C:/Desarrollo/Scripts-varios/Originales/'

# Verificar si el directorio contiene archivos PDF
archivos_pdf = [archivo for archivo in os.listdir(directorio) if archivo.endswith('.pdf')]
if not archivos_pdf:
    print("No se encontraron archivos PDF en el directorio")
    exit()

# Procesar cada archivo PDF en el directorio
for archivo in archivos_pdf:
    archivo_pdf = os.path.join(directorio, archivo)
    print(f"Procesando archivo: {archivo}")

    # Abrir el archivo PDF
    with open(archivo_pdf, 'rb') as archivo_pdf_abierto:
        pdf = PyPDF2.PdfReader(archivo_pdf_abierto)
        print(f"Archivo PDF abierto correctamente. Número de páginas: {len(pdf.pages)}")

        # Extraer el texto del PDF
        texto = ''
        for pagina in range(len(pdf.pages)):
            texto += pdf.pages[pagina].extract_text()

        # Crear un HTML con el texto
        html = f"<html><body><p>{texto}</p></body></html>"

        # Crear un PDF con el resultado
        nombre_original = os.path.splitext(archivo)[0]
        archivo_salida = os.path.join(directorio, f'{nombre_original}_resultado.pdf')
        print(f"Creando PDF con resultado: {archivo_salida}")

        # Utilizar pdfkit para convertir el HTML a PDF
        opciones = {
            'page-size': 'Letter',
            'margin-top': '0.75in',
            'margin-right': '0.75in',
            'margin-bottom': '0.75in',
            'margin-left': '0.75in',
            'encoding': "UTF-8",
            'no-outline': None
        }
        pdfkit.from_string(html, archivo_salida, opciones)

print("Proceso finalizado")