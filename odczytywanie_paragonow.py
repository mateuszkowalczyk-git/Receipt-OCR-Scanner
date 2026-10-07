import re
import os
import pandas as pd
from PIL import Image, ImageEnhance, ImageFilter
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def save_to_excel(date_list, price_list, store_name, filename="Wydatki_Paragony.xlsx"):
    # Wybieramy pierwszą datę, lub wpisujemy "Brak danych"
    receipt_date = date_list[0] if date_list else "Brak danych"
    
    # Wybieramy najwyższą kwotę z paragonu (zazwyczaj jest to suma całkowita)
    # Zmieniamy najpierw stringi typu '89,90' na float 89.90
    if price_list:
        prices_float = [float(p.replace(',', '.')) for p in price_list]
        total_price = max(prices_float)
    else:
        total_price = 0.0

    # Tworzymy słownik z naszymi danymi (jeden wiersz)
    data = {
        "Data": [receipt_date],
        "Sklep": [store_name],
        "Suma (PLN)": [total_price]
    }
    df = pd.DataFrame(data)

    # Sprawdzamy czy plik już istnieje, aby dopisać dane, a nie go nadpisać
    if os.path.exists(filename):
        # Wczytaj stary plik i połącz z nowymi danymi
        existing_df = pd.read_excel(filename)
        updated_df = pd.concat([existing_df, df], ignore_index=True)
    else:
        # Jeśli nie istnieje, zrób nowy
        updated_df = df

    # Zapisz do excela
    updated_df.to_excel(filename, index=False)
    print(f"[*] Sukces! Zapisano dane do pliku {filename}")


def analyze_receipt(image_path):
    print(f"[*] Przetwarzanie pliku: {image_path}...")
    
    try:
        img = Image.open(image_path)
    except FileNotFoundError:
        print(f"[!] Błąd: Nie znaleziono pliku {image_path}")
        return

    # Preprocessing
    img = img.resize((img.width * 2, img.height * 2), Image.Resampling.LANCZOS)
    img = img.convert('L')
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(3.0)
    img = img.filter(ImageFilter.SHARPEN)

    # OCR
    custom_config = r'--oem 3 --psm 4'
    text = pytesseract.image_to_string(img, lang='pol', config=custom_config)
    
    # Parsowanie RegEx
    prices = re.findall(r'\b\d+[\.,]\d{2}\b', text)
    
    # Rozszerzamy regex dla daty, aby złapał również daty w innych formatach 
    # (np. Twoja z OCR miała kropki i myślniki lub była ucięta - tu szukamy ogólnego wzorca)
    dates = re.findall(r'\b20\d{2}[-\.]\d{2}[-\.]\d{2}\b', text)
    
    # Próbujemy wyciągnąć pierwszą linijkę tekstu (często to nazwa sklepu)
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    store_name = lines[0] if lines else "Nieznany sklep"

    print(f"--- WYPARSOWANE DANE ---")
    print(f"Sklep: {store_name}")
    print(f"Daty: {dates}")
    print(f"Kwoty: {prices}")
    print("------------------------")

    # Uruchamiamy funkcję zapisującą!
    save_to_excel(dates, prices, store_name)

if __name__ == "__main__":
    analyze_receipt("paragon.jpeg")