from deep_translator import GoogleTranslator

class Translator:
    def __init__(self, source='auto', target='es'):
        """
        Initializes a Translator object to translate text from one language to another.

        Args:
            source (str, optional): The source language code. Defaults to 'auto'.
            target (str, optional): The target language code. Defaults to 'es'.
        """

        self.translator = GoogleTranslator(source=source, target=target)
        self.chunk_size = 2000

    def _translate_chunk(self, chunk):
        """
        Translates a chunk of text using the translator.

        Args:
            chunk (str): A chunk of text to translate.

        Returns:
            str: The translated text.
        """

        return self.translator.translate(chunk)

    def translate(self, text):
        """
        Translates a given text by dividing it into manageable chunks and translating each chunk.

        Args:
            text (str): The text to be translated.

        Returns:
            str: The translated text obtained by concatenating the translated chunks.
        """
        chunks = [text[i:i + self.chunk_size] for i in range(0, len(text), self.chunk_size)]
        translated_chunks = [self._translate_chunk(chunk) for chunk in chunks]
        return ''.join(translated_chunks)