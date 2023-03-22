from pojistenec import Pojistenec


class Databaze:
    """
    Třída pro práci s databází pojištěných.
    """
    _databaze_pojistencu = {}

    def __init__(self):
        pass

    def pridej_pojisteneho(self):
        jmeno = input("Zadejte jméno pojištěnce:\n")
        prijmeni = input("Zadejte příjmení pojištěnce:\n")
        telefon = input("Zadejte telefonní číslo:\n")
        vek = input("Zadejte věk:\n")
        novy_pojistenec = Pojistenec(jmeno, prijmeni, telefon, vek)
        self._databaze_pojistencu.update({jmeno+prijmeni: novy_pojistenec})
        input("Data byla uložena. Pokračujte stiskem libovolné klávesy...") 
        #back to menu

    def vypis_pojistene(self):
        if len(self._databaze_pojistencu) == 0:
            print("Seznam pojištěných je prázdný.")
        else:
            for pojisteny in self._databaze_pojistencu:
                print(self._databaze_pojistencu[pojisteny])
            input("Pokračujte libovolnou klávesou...") 
            #back to menu

    def vyhledej_pojisteneho(self):
        jmeno = input("Zadejte jméno pojištěnce:\n")
        prijmeni = input("Zadejte příjmení pojištěnce:\n")
        if jmeno+prijmeni in self._databaze_pojistencu:
            print((self._databaze_pojistencu[jmeno+prijmeni]))
        else:
            print("Pojištěnec nebyl nalezen.")
        input("Pokračujte libovolnou klávesou...") 
        #back to menu
