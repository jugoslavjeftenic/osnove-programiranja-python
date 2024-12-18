import os; os.system("cls")

# Funkcija: zamijeni_samoglasnike Napisati funkciju zamijeni_samoglasnike koja prima string i
# zamjenjuje sve samoglasnike (a, e, i, o, u) sa karakterom *.
# Na primjer, poziv zamijeni_samoglasnike("programiranje") treba da vrati pr*gr*m*r*nj*.

def zamijeni_samoglasnike(tekst):
    zamijenjeni_tekst = ""
    for i in tekst:
        match i:
            case "a" | "e" | "i" | "o" | "u":
                zamijenjeni_tekst += "*"
            case _:
                zamijenjeni_tekst += i
    return zamijenjeni_tekst

print(zamijeni_samoglasnike("programiranje"))
