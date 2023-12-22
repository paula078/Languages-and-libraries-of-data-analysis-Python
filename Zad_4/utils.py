import json

def zapisz_dane(sciezka_uzytkownicy, sciezka_ksiazki, uzytkownicy, ksiazki):
    with open(sciezka_uzytkownicy, 'w') as plik_uzytkownicy, open(sciezka_ksiazki, 'w') as plik_ksiazki:
        json.dump(uzytkownicy, plik_uzytkownicy, indent=2)
        json.dump(ksiazki, plik_ksiazki, indent=2)

def wczytaj_dane(sciezka_uzytkownicy, sciezka_ksiazki):
    try:
        with open(sciezka_uzytkownicy, 'r') as plik_uzytkownicy, open(sciezka_ksiazki, 'r') as plik_ksiazki:
            return json.load(plik_uzytkownicy), json.load(plik_ksiazki)
    except FileNotFoundError:
        print("Pliki z danymi nie istnieją. Tworzę nowe puste pliki.")
        zapisz_dane(sciezka_uzytkownicy, sciezka_ksiazki, {}, {})
        return {}, {}
