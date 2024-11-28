import os; os.system("cls")

# Funkcija: zamijeni_razmake Napisati funkciju zamijeni_razmake koja prima string i
# zamjenjuje sve razmake u tom stringu sa podvlakom _.
# Na primjer, poziv zamijeni_razmake("Ovo je primjer") treba da vrati Ovo_je_primjer.

def zamijeni_razmake(tekst):
    zamijenjeni_tekst = ""
    for i in tekst:
        if i == " ":
            zamijenjeni_tekst += "_"
            continue
        zamijenjeni_tekst += i
    return zamijenjeni_tekst

print(zamijeni_razmake("Petar Petrovic Petronije"))
