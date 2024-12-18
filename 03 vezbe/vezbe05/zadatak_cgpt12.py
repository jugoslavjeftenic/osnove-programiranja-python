import os; os.system("cls")

# Funkcija: broj_karaktera Napisati funkciju broj_karaktera koja prima string i jedan karakter c,
# te vraća broj pojavljivanja tog karaktera c u stringu.
# Na primjer, poziv broj_karaktera("banana", "a") treba da vrati 3.

def broj_karaktera(tekst, slovo):
    brojac = 0
    for i in tekst:
        if i == slovo:
            brojac += 1
    return brojac

print(broj_karaktera("Petar Petrovic", "e"))
