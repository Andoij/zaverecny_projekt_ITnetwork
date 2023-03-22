from databaze import Databaze


"""
Spouštění aplikace.
"""

databaze = Databaze


def menu():
    """
    Textová reprezentaci úvodního menu s volbami 1-4.
    """
    print("----------------------------")
    print("Evidence pojištěných")
    print("----------------------------")
    print()
    print("Vyberte si akci:")
    print("1 - Přidat nového pojištěného")
    print("2 - Vypsat všechny pojištěné")
    print("3 - Vyhledat pojištěnou osobu")
    print("4 - Konec")
    cislo_akce = kontrola_volby("", "Neplatné zadání!\n")
    zvol_si(cislo_akce)


def kontrola_volby(text_zadani, text_chyba):
    """
    Kontrola správnosti vstupu uživatele. Správné hodnoty pouze 1-4.
    """
    spatne = True
    cislo = int(input(text_zadani))
    while spatne:
        try:
            assert 0 < cislo < 5
            spatne = False
        except ValueError:
            print(text_chyba)
            menu()
        except AssertionError:
            print(text_chyba)
            menu()
    else:
        return cislo


def zvol_si(cislo_akce):
    """
    Volba funkce databáze.
    """
    if cislo_akce == 1:
        databaze.pridej_pojisteneho(Databaze)
        menu()
    elif cislo_akce == 2:
        databaze.vypis_pojistene(Databaze)
        menu()
    elif cislo_akce == 3:
        databaze.vyhledej_pojisteneho(Databaze)
        menu()
    else:
        exit()


menu()