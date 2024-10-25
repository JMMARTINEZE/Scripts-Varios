from deep_translator import GoogleTranslator

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