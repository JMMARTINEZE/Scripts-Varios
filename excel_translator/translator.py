import pandas as pd
from deep_translator import GoogleTranslator
from tqdm import tqdm

class Translator:
    def __init__(self, source='auto', target='es'):
        self.translator = GoogleTranslator(source=source, target=target)
        self.chunk_size = 2000

    def _translate_chunk(self, chunk):
        return self.translator.translate(chunk)

    def translate(self, text):
        chunks = [text[i:i + self.chunk_size] for i in range(0, len(text), self.chunk_size)]
        translated_chunks = [self._translate_chunk(chunk) for chunk in chunks]
        return ''.join(translated_chunks)
    
    def translate_excel(self, input_file, output_file):
        # Leer el archivo Excel
        df = pd.read_excel(input_file)
    
        # Traducir el contenido
        translated_data = []
        total_rows = len(df)
        for index, row in tqdm(df.iterrows(), total=total_rows, desc="Traduciendo"):
            translated_row = []
            for cell in row:
                if isinstance(cell, str) and len(cell.strip()) > 0:
                    translated_cell = self.translate(cell)
                    translated_row.append(translated_cell)
                else:
                    translated_row.append(cell)
            translated_data.append(translated_row)
    
        # Escribir el resultado en un nuevo archivo Excel
        translated_df = pd.DataFrame(translated_data, columns=df.columns)
        translated_df.to_excel(output_file, index=False)

translator = Translator()
translator.translate_excel('MDM_INGLES.xlsx', 'MDM_ESPANOL.xlsx')