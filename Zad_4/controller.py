from datetime import datetime, timedelta

# --------------- LOGOWANIE --------------------
def zaloguj(uzytkownicy, login_czytelnika):

    while True:
        login = input("Podaj login: ")
        haslo = input("Podaj hasło: ")

        if login in uzytkownicy and uzytkownicy[login]['haslo'] == haslo:
            if login == 'bibliotekarz':
                zalogowany_uzytkownik = 'bibliotekarz'
                print("Zalogowano jako bibliotekarz.")
                break
            else:
                zalogowany_uzytkownik = 'czytelnik'
                login_czytelnika = login
                print("Zalogowano jako czytelnik.")
                break
        else:
            print("Błędny login lub hasło. Spróbuj ponownie.")
    return zalogowany_uzytkownik, login_czytelnika


# --------------- CZYTELNIK --------------------
def wypozycz_ksiazke(ksiazki, login_czytelnika):
    tytul = input("Podaj tytuł książki do wypożyczenia: ")

    if tytul in ksiazki:
        status = ksiazki[tytul]["status"]
        czytelnik = ksiazki[tytul].get("czytelnik")

        if status == "dostepna" or (status == "zarezerwowana" and czytelnik == login_czytelnika):
            ksiazki[tytul]["status"] = "wypozyczona"
            ksiazki[tytul]["czytelnik"] = login_czytelnika
            ksiazki[tytul]["data_wypozyczenia"] = datetime.now().strftime("%Y-%m-%d")
            # Wypozyczenie na 20 dni
            data_wypozyczenia = datetime.strptime(ksiazki[tytul]["data_wypozyczenia"], "%Y-%m-%d")
            ksiazki[tytul]["data_zwrotu"] = (data_wypozyczenia + timedelta(days=20)).strftime("%Y-%m-%d")
            print(f"Wypożyczono książkę: {tytul}")

        elif status == "zarezerwowana" and czytelnik != login_czytelnika:
            print(f"Książka o podanym tytule jest zarezerwowana przez innego czytelnika.")
        else:
            print(f"Książka o podanym tytule nie jest dostępna.")
    else:
        print("Książka o podanym tytule nie istnieje.")


def zarezerwuj_ksiazke(ksiazki, login_czytelnika):
    tytul = input("Podaj tytuł książki do zarezerwowania: ")

    if tytul in ksiazki:
        status = ksiazki[tytul]["status"]
        czytelnik = ksiazki[tytul].get("czytelnik")
        zarezerwowane = ksiazki[tytul].get("zarezerwowane", [])

        if status == "wypozyczona" and czytelnik != login_czytelnika:
            czytelnik_rezerwacje = [rez['czytelnik'] for rez in zarezerwowane]
            if login_czytelnika not in czytelnik_rezerwacje:
                if "zarezerwowane" not in ksiazki[tytul]:
                    ksiazki[tytul]["zarezerwowane"] = [
                        {"czytelnik": login_czytelnika, "data_rezerwacji": datetime.now().strftime("%Y-%m-%d")}]
                else:
                    ksiazki[tytul]["zarezerwowane"].append(
                        {"czytelnik": login_czytelnika, "data_rezerwacji": datetime.now().strftime("%Y-%m-%d")})
                print(f"Zarezerwowano książkę: {tytul}")
        elif status == "wypozyczona" and czytelnik == login_czytelnika:
            print(f"Nie możesz zarezerwować książki, którą masz wypożyczoną.")
        else:
            print(f"Książka o podanym tytule jest dostępna.")
    else:
        print("Książka o podanym tytule nie istnieje.")

def przedluz_wypozyczenie(ksiazki, login_czytelnika):
    tytul = input("Podaj tytuł książki do przedłużenia wypożyczenia: ")

    if tytul in ksiazki and ksiazki[tytul]["status"] == "wypozyczona" and ksiazki[tytul]["czytelnik"] == login_czytelnika:
        if "ilosc_przedluzen" not in ksiazki[tytul]:
            ksiazki[tytul]["ilosc_przedluzen"] = 0

        if ksiazki[tytul]["ilosc_przedluzen"] < 3:
            # Przedłużenie o 20 dni
            nowa_data = datetime.strptime(ksiazki[tytul]["data_zwrotu"], "%Y-%m-%d")
            ksiazki[tytul]["data_zwrotu"] = (nowa_data + timedelta(days=20)).strftime("%Y-%m-%d")
            ksiazki[tytul]["ilosc_przedluzen"] += 1
            print(f"Przedłużono wypożyczenie książki: {tytul}")
        else:
            print("Książki nie można przedłużyć więcej niż 3 razy.")
    else:
        print("Książka o podanym tytule nie istnieje lub nie jest wypożyczona przez Ciebie.")


# --------------- BIBLIOTEKARZ --------------------
def dodaj_czytelnika(uzytkownicy):
    login = input("Podaj login nowego czytelnika: ")

    if login in uzytkownicy:
        print("Czytelnik o podanym loginie już istnieje.")
    else:
        haslo = input("Podaj hasło nowego czytelnika: ")
        imie = input("Podaj imię nowego czytelnika: ")
        nazwisko = input("Podaj nazwisko nowego czytelnika: ")

        uzytkownicy[login] = {'haslo': haslo, 'imie': imie, 'nazwisko': nazwisko}
        print("Dodano nowego czytelnika.")

def dodaj_ksiazke(ksiazki):
    tytul = input("Podaj tytuł książki: ")

    if tytul in ksiazki:
        print("Książka o podanym tytule już istnieje.")
    else:
        autor = input("Podaj autora książki: ")
        status = "dostepna"
        ksiazki[tytul] = {"autor": autor, "status": status}
        print(f"Dodano nową książkę: {tytul} - {autor}")

def usun_ksiazke(ksiazki):
    tytul = input("Podaj tytuł książki do usunięcia: ")

    if tytul in ksiazki:
        del ksiazki[tytul]
        print(f"Usunięto książkę o tytule: {tytul}")
    else:
        print("Książka o podanym tytule nie istnieje.")

def przyjmij_zwrot(ksiazki):
    tytul = input("Podaj tytuł książki do zwrotu: ")

    if tytul in ksiazki and ksiazki[tytul]["status"] == "wypozyczona":
        ksiazki[tytul]["status"] = "dostepna"
        ksiazki[tytul].pop("czytelnik", None)
        ksiazki[tytul].pop("ilosc_przedluzen", None)
        ksiazki[tytul].pop("data_wypozyczenia", None)
        ksiazki[tytul].pop("data_zwrotu", None)
        ksiazki[tytul].pop("zarezerwowane", None)
        print(f"Przyjęto zwrot książki: {tytul}")
    else:
        print("Książka o podanym tytule nie jest obecnie wypożyczona lub nie istnieje.")
