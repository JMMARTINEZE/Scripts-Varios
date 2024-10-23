import os
import json
import chardet
from deep_translator import GoogleTranslator
from docx import Document

# Detectar la codificación del archivo
def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        raw_data = f.read(10000)  # Leer los primeros 10,000 bytes
    result = chardet.detect(raw_data)
    return result['encoding']

# Ruta del archivo JSON y la plantilla de Word
json_filepath = os.path.join(os.path.dirname(__file__), "./data.json")
template_filepath = os.path.join(os.path.dirname(__file__), "./template.docx")

# Detectar la codificación del archivo JSON
encoding = detect_encoding(json_filepath)
print(f"Codificación detectada: {encoding}")

# Leer el archivo JSON con la codificación detectada
with open(json_filepath, 'r', encoding=encoding) as i18n_file:
    parsed_json = json.load(i18n_file)

# Traductor
translator = GoogleTranslator(source='auto', target='es')

# Cargar el documento Word existente como plantilla
doc = Document(template_filepath)

# Verificar si parsed_json es un diccionario o una lista
if isinstance(parsed_json, dict) and "Results" in parsed_json:
    results = parsed_json["Results"]
    for group in results.values():
        for original in group:
            doc.add_heading(original['GroupName'], level=2)  # Usar el nombre del grupo como título 2
            
            for control in original.get('Controls', []):
                for field, value in control.items():
                    translated_title = translator.translate(field)
                    doc.add_heading(translated_title, level=3)  # Añadir como título 3 en el documento
                    translated_content = translator.translate(value)
                    doc.add_paragraph(translated_content)

elif isinstance(parsed_json, list):
    for original in parsed_json:
        doc.add_heading(original['FindingName'], level=2)  # Usar el nombre del hallazgo como título 2
        
        for field, value in original.items():
            # Ignorar el campo ID y el FindingName
            if field == 'ID' or field == 'FindingName':
                continue
            
            translated_title = translator.translate(field)
            doc.add_heading(translated_title, level=3)  # Añadir como título 3 en el documento
            translated_content = translator.translate(value)
            doc.add_paragraph(translated_content)

# Guardar el documento respetando la plantilla original
output_filepath = os.path.join(os.path.dirname(__file__), "traducciones_respetando_plantilla.docx")
doc.save(output_filepath)

print(f"Documento guardado en: {output_filepath}")