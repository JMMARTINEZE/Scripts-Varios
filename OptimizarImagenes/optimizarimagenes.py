import os
from PIL import Image

# Configuración
CARPETA_ENTRADA = os.path.join(os.path.dirname(__file__), 'input')
CARPETA_SALIDA = os.path.join(os.path.dirname(__file__), 'output')
ANCHO_MAXIMO = 1920
CALIDAD_WEBP = 80  # calidad recomendada para webp

# Crear carpeta de salida si no existe
os.makedirs(CARPETA_SALIDA, exist_ok=True)

# Procesar imágenes
for archivo in os.listdir(CARPETA_ENTRADA):
    if archivo.lower().endswith(('.png', '.jpg', '.jpeg')):
        ruta_entrada = os.path.join(CARPETA_ENTRADA, archivo)

        # Quitar extensión para nuevo nombre
        nombre_sin_extension = os.path.splitext(archivo)[0]
        ruta_salida = os.path.join(CARPETA_SALIDA, f"{nombre_sin_extension}.webp")

        with Image.open(ruta_entrada) as img:
            img = img.convert("RGB")  # convertir a RGB si no lo está
            # Redimensionar si es necesario
            if img.width > ANCHO_MAXIMO:
                nuevo_alto = int((ANCHO_MAXIMO / img.width) * img.height)
                img = img.resize((ANCHO_MAXIMO, nuevo_alto), Image.LANCZOS)

            # Guardar como .webp optimizado
            img.save(ruta_salida, format='WEBP', quality=CALIDAD_WEBP, method=6)

        # Borrar el original
        os.remove(ruta_entrada)

print(" Todas las imágenes han sido optimizadas y se han eliminado los originales. Las nuevas imágenes han sido convertidas a .webp.")
