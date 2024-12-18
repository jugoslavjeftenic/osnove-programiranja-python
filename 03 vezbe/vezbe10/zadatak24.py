import os; os.system("cls")

def provjeri(recnik):
    return all(len(kljuc) == vrednost for kljuc, vrednost in recnik.items())

print("Vrednosti odgovaraju duzini kljuceva:", provjeri({"Ana":3, "Pera":4, "Iva":3}))
print("Vrednosti odgovaraju duzini kljuceva:", provjeri({"Ana":3, "Pera":7, "Iva":3}))
