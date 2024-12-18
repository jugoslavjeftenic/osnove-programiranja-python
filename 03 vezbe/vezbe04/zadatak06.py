import os; os.system("cls")

def unos_podataka():
    ime = input("Unesite ime: ")
    prezime = input("Unesite prezime: ")
    godine = int(input("Unesite godine: "))
    return ime, prezime, godine

print(unos_podataka())
