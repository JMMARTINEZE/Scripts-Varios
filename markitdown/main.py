import os
from markitdown import MarkItDown

archivo = '../Originales/CIS_Fortigate_Benchmark_v1.1.0.pdf'
nombre_archivo_md = archivo.replace('.pdf', '.md')
markitdown = MarkItDown()
result = markitdown.convert(archivo)

print(f"Guardando archivo en: {os.path.abspath(nombre_archivo_md)}")

with open(nombre_archivo_md, 'w') as f:
    f.write(result.text_content.replace('\u25cf', '\u002A').replace('\uf06f', '\u002A'))

