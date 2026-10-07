Receipt OCR Scanner

Prosty skrypt w jezyku Python sluzacy do automatycznego odczytywania i analizowania danych z paragonow za pomoca technologii OCR. Skrypt wyciaga z obrazu nazwe sklepu, date zakupu oraz laczna kwote, a nastepnie zapisuje te dane do arkusza kalkulacyjnego Excel.

Funkcjonalnosci

Preprocessing obrazu (Pillow): automatyczne powiekszanie, zmiana na skale szarosci, podbicie kontrastu i wyostrzanie w celu poprawy dokladnosci OCR.

Rozpoznawanie tekstu (Tesseract OCR): czytanie tekstu w trybie kolumnowym z obsluga jezyka polskiego.

Ekstrakcja danych (Wyrazenia regularne): parsowanie zaszumionego tekstu w poszukiwaniu dat i kwot.

Eksport danych (Pandas): automatyczne tworzenie i aktualizowanie pliku Wydatki_Paragony.xlsx o nowe pozycje.

Wymagania systemowe

Python 3.x

Silnik Tesseract OCR zainstalowany w systemie operacyjnym (wraz z paczka jezyka polskiego).

Domyslna sciezka w systemie Windows, ktorej szuka skrypt to: C:\Program Files\Tesseract-OCR\tesseract.exe

Instalacja

Zainstaluj wymagane biblioteki Pythona uzywajac menedzera pakietow pip:

pip install pytesseract Pillow pandas openpyxl

Uzycie

Umiesc zdjecie paragonu w folderze ze skryptem (np. paragon.jpeg).

Upewnij sie, ze nazwa pliku w kodzie (w sekcji main) zgadza sie z nazwa Twojego zdjecia.

Uruchom skrypt z poziomu terminala:

python odczytywanie_paragonow.py

Po zakonczeniu dzialania programu, w folderze pojawi sie zaktualizowany plik Wydatki_Paragony.xlsx zawierajacy 
