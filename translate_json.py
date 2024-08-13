import json
import logging
from deep_translator import GoogleTranslator

# Log ayarlarını yap
logging.basicConfig(filename='translation_log.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# JSON dosyasını oku
with open('language_file.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Çevirici başlat
translator = GoogleTranslator(source='en', target='tr')

# JSON verilerini Türkçeye çevir
def translate_to_turkish(data):
    if isinstance(data, dict):
        return {key: translate_to_turkish(value) for key, value in data.items()}
    elif isinstance(data, list):
        return [translate_to_turkish(element) for element in data]
    elif isinstance(data, str):
        try:
            translated = translator.translate(data)
            # Çeviri kaydını logla
            logging.info(f"Orijinal: {data} -> Çeviri: {translated}")
            return translated
        except Exception as e:
            # Hata oluşursa logla
            logging.error(f"Çeviri hatası: {str(e)} için metin: {data}")
            return data  # Hata durumunda orijinal metni döndür
    else:
        return data

# Çeviri işlemi
translated_data = translate_to_turkish(data)

# Türkçe çevrilmiş JSON verisini kaydet
with open('translated_language_file.json', 'w', encoding='utf-8') as file:
    json.dump(translated_data, file, ensure_ascii=False, indent=4)

print("Çeviri işlemi tamamlandı ve dosya kaydedildi.")
