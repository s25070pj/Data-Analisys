# Data Analyzer

Data Analyzer to aplikacja do analizy danych z wykorzystaniem bibliotek NumPy, Pandas, Matplotlib oraz Seaborn. Aplikacja umożliwia wczytanie zbioru danych, jego eksplorację oraz generowanie różnorodnych wykresów. Projekt został stworzony jako zadanie zaliczeniowe na studia.

## Funkcjonalności

- Wczytywanie plików CSV
- Wyświetlanie danych w tabeli z pionowym i poziomym przewijaniem
- Filtrowanie danych według wartości tekstowych
- Filtrowanie danych według zakresów liczbowych
- Resetowanie filtrów
- Sortowanie danych
- Generowanie wykresów słupkowych, kołowych oraz zaawansowanych wykresów
- Komunikowanie podstawowych wniosków z analizy danych

## Instalacja

1. Skopiuj repozytorium projektu na swój komputer.
2. Przejdź do katalogu projektu.
3. Zainstaluj wymagane biblioteki:
   pip install -r requirements.txt
4. Uruchom aplikację: python main.py
5. Załaduj plik CSV, klikając przycisk "Load CSV".
6. Użyj dostępnych opcji do filtrowania i sortowania danych.
7. Wybierz typ wykresu z rozwijanego menu i kliknij przycisk "Plot", aby wygenerować wykres.

## Wyjaśnienie metod i rozwiązań programistycznych
- Metody analizy danych
1. Filtrowanie danych: Pozwala użytkownikowi na filtrowanie danych według wartości tekstowych oraz zakresów liczbowych. Jest to przydatne w przypadku dużych zbiorów danych, gdzie potrzebne są tylko określone informacje.
2. Sortowanie danych: Umożliwia sortowanie danych według wybranej kolumny, co ułatwia analizę i porównywanie wartości.
- Wizualizacja danych
1. Wykresy słupkowe: Używane do prezentacji rozkładu danych kategorycznych. Jest to odpowiednie do wizualizacji częstotliwości różnych kategorii.
2. Wykresy kołowe: Używane do prezentacji udziałów procentowych poszczególnych kategorii. Jest to przydatne do pokazania proporcji każdej kategorii w zbiorze danych.
3. Zaawansowane wykresy (Pairplot): Używane do wizualizacji relacji pomiędzy wieloma zmiennymi numerycznymi jednocześnie. Jest to przydatne do identyfikacji korelacji i wzorców w danych.