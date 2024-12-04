import os
import re
from PyPDF2 import PdfReader
from tqdm import tqdm

# Crear un archivo CSV vacío
output_file = "policies.csv"
with open(output_file, "w") as file:
    file.write("Policy,Profile Applicability,Description,Rationale,Impact,Audit,Remediation,Default Value\n")

# Leer el PDF y extraer el texto
pdf_path = "input.pdf"
text = ""
with open(pdf_path, "rb") as pdf_file:
    pdf = PdfReader(pdf_file)
    for page in pdf.pages:
        text += page.extract_text()

# Variables para almacenar temporalmente cada sección
policy = ""
profile_applicability = ""
description = ""
rationale = ""
impact = ""
audit = ""
remediation = ""
default_value = ""
title = ""
capture_section = ""  # Inicializar capture_section aquí

# Procesar el texto extraído del PDF
lines = text.split("\n")
num_lines = len(lines)
for line in tqdm(lines, desc="Processing PDF"):
    line = line.strip()
    if line.endswith(":"):
        header = line[:-1]
        if header == "Profile Applicability":
            capture_section = "profile_applicability"
            # Extraer el título desde la línea anterior
            title_match = re.search(r'\((.*?)\)', title)
            if title_match:
                title = title_match.group(1)
        else:
            capture_section = header.lower().replace(" ", "_")
    else:
        if capture_section:
            # Añadir la línea al contenido actual
            if capture_section == "policy":
                title = line.split("->")[0].strip()
                policy = line.split("->")[1].strip()
            else:
                # Verificar si la clave está presente en locals() antes de acceder a ella
                if capture_section not in locals():
                    locals()[capture_section] = ""
                locals()[capture_section] += line + " "

    # Detectar fin de una política (cuando la línea siguiente esté vacía)
    if not line:
        with open(output_file, "a") as out_file:
            out_file.write(f"{policy},\"{title}\",\"{description}\",\"{rationale}\",\"{impact}\",\"{audit}\",\"{remediation}\",\"{default_value}\"\n")

        # Reiniciar variables
        policy = ""
        profile_applicability = ""
        description = ""
        rationale = ""
        impact = ""
        audit = ""
        remediation = ""
        default_value = ""
        title = ""
        capture_section = ""  # Reinicializar capture_section al final de cada sección

# Eliminar archivo temporal
# os.remove("temp.txt")