import controller

def przegladaj_katalog(ksiazki):
    print("Opcje przeglądania katalogu:")
    print("1. Przeglądaj wszystkie książki")
    print("2. Wyszukaj po tytule")
    print("3. Wyszukaj po autorze")
    print("4. Wyszukaj po słowach kluczowych")
    opcja = input("Wybierz opcję: ")

    if opcja == '1':
        wyswietl_ksiazki(ksiazki)
    elif opcja == '2':
        tytul = input("Podaj tytuł książki do wyszukania: ")
        wyszukaj_ksiazki('tytul', tytul, ksiazki)
    elif opcja == '3':
        autor = input("Podaj autora książki do wyszukania: ")
        wyszukaj_ksiazki('autor', autor, ksiazki)
    elif opcja == '4':
        slowa_kluczowe = input("Podaj słowa kluczowe do wyszukania: ")
        wyszukaj_ksiazki('slowa_kluczowe', slowa_kluczowe, ksiazki)
    else:
        print("Nieprawidłowa opcja.")

def wyswietl_ksiazki(ksiazki):
    for tytul, info in ksiazki.items():
        print(f"Tytuł: {tytul}")
        print(f"Autor: {info['autor']}")
        print(f"Status: {info['status']}")
        if 'czytelnik' in info:
            print(f"Czytelnik: {info['czytelnik']}")
        if 'data_wypozyczenia' in info:
            print(f"Data wypożyczenia: {info['data_wypozyczenia']}")
        if 'data_zwrotu' in info:
            print(f"Data zwrotu: {info['data_zwrotu']}")
        if 'ilosc_przedluzen' in info:
            print(f"Ilość przedłużeń: {info['ilosc_przedluzen']}")
        if 'zarezerwowane' in info:
            print(f"Rezerwacje: {info['zarezerwowane']}")
        print("------")

def wyszukaj_ksiazki(kryterium, wartosc, ksiazki):
    znalezione_ksiazki = {}
    for tytul, info in ksiazki.items():
        if kryterium == 'tytul' and wartosc.lower() in tytul.lower():
            znalezione_ksiazki[tytul] = info
        elif kryterium == 'autor' and wartosc.lower() in info['autor'].lower():
            znalezione_ksiazki[tytul] = info
        elif kryterium == 'slowa_kluczowe' and wartosc.lower() in (tytul.lower() + info['autor'].lower()):
            znalezione_ksiazki[tytul] = info

    if znalezione_ksiazki:
        wyswietl_ksiazki(znalezione_ksiazki)
    else:
        print("Brak pasujących książek.")
        
#------------MENU------------

def menu_czytelnika(zalogowany_uzytkownik, ksiazki, login_czytelnika):
    print("Menu czytelnika:")
    print("1. Wypożycz książkę")
    print("2. Zarezerwuj książkę")
    print("3. Przedłuż wypożyczenie")
    print("4. Przeglądaj katalog")
    print("5. Wyloguj")
    wybor = input("Wybierz opcję: ")

    if wybor == '1':
        controller.wypozycz_ksiazke(ksiazki, login_czytelnika)
    elif wybor == '2':
        controller.zarezerwuj_ksiazke(ksiazki, login_czytelnika)
    elif wybor == '3':
        controller.przedluz_wypozyczenie(ksiazki, login_czytelnika)
    elif wybor == '4':
        przegladaj_katalog(ksiazki)
    elif wybor == '5':
        zalogowany_uzytkownik = None
    else:
        print("Nieprawidłowy wybór. Spróbuj ponownie.")

    return zalogowany_uzytkownik

def menu_bibliotekarza(zalogowany_uzytkownik, ksiazki, uzytkownicy):
    print("Menu bibliotekarza:")
    print("1. Dodaj czytelnika")
    print("2. Dodaj książkę")
    print("3. Usuń książkę")
    print("4. Przeglądaj katalog")
    print("5. Przyjmij zwrot książki")
    print("6. Wyloguj")
    wybor = input("Wybierz opcję: ")

    if wybor == '1':
        controller.dodaj_czytelnika(uzytkownicy)
    elif wybor == '2':
        controller.dodaj_ksiazke(ksiazki)
    elif wybor == '3':
        controller.usun_ksiazke(ksiazki)
    elif wybor == '4':
        przegladaj_katalog(ksiazki)
    elif wybor == '5':
        controller.przyjmij_zwrot(ksiazki)
    elif wybor == '6':
        zalogowany_uzytkownik = None
        print("Wylogowano.")
    else:
        print("Nieprawidłowy wybór. Spróbuj ponownie.")
    return zalogowany_uzytkownik
