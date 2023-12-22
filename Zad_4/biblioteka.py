import json
from pathlib import Path
from datetime import datetime, timedelta
import utils
import view
import controller

class Biblioteka:
    def __init__(self):
        self.katalog_danych = Path('./dane')
        self.sciezka_uzytkownicy = self.katalog_danych / 'uzytkownicy.json'
        self.sciezka_ksiazki = self.katalog_danych / 'ksiazki.json'

        self.uzytkownicy = {}
        self.ksiazki = {}
        self.zalogowany_uzytkownik = None
        self.login_czytelnika = None

    def wczytaj_dane(self):
        self.uzytkownicy, self.ksiazki = utils.wczytaj_dane(self.sciezka_uzytkownicy, self.sciezka_ksiazki)

    def zapisz_dane(self):
        utils.zapisz_dane(self.sciezka_uzytkownicy, self.sciezka_ksiazki, self.uzytkownicy, self.ksiazki)


if __name__ == "__main__":
    biblioteka = Biblioteka()
    biblioteka.wczytaj_dane()

    while True:
        if biblioteka.zalogowany_uzytkownik is None:
            print("1. Zaloguj")
            print("2. Wyjdź")
            wybor = input("Wybierz opcję: ")

            if wybor == '1':
                biblioteka.zalogowany_uzytkownik, biblioteka.login_czytelnika = controller.zaloguj(biblioteka.uzytkownicy, biblioteka.login_czytelnika)

            elif wybor == '2':
                break
            else:
                print("Nieprawidłowy wybór. Spróbuj ponownie.")
        elif biblioteka.zalogowany_uzytkownik == 'czytelnik':
            biblioteka.zalogowany_uzytkownik = view.menu_czytelnika(biblioteka.zalogowany_uzytkownik, biblioteka.ksiazki, biblioteka.login_czytelnika)
        elif biblioteka.zalogowany_uzytkownik == 'bibliotekarz':
            biblioteka.zalogowany_uzytkownik = view.menu_bibliotekarza(biblioteka.zalogowany_uzytkownik, biblioteka.ksiazki, biblioteka.uzytkownicy)

    biblioteka.zapisz_dane()
