!pip install googletrans==4.0.0-rc1

from googletrans import Translator

translator = Translator()

def translate_to_hindi(text: str) -> str:
    """Translate English text to Hindi using Google Translate API."""
    return translator.translate(text, src='en', dest='hi').text
