import os; os.system("cls")

# Funkcija: zameni_slova Napisati funkciju zameni_slova koja prima dva karaktera x i y.
# Unutar funkcije od korisnika se traži da unese neki string,
# a zatim se u stringu karakter x zamjenjuje karakterom y. Funkcija vraća tako dobijen string.

def zameni_slova(x, y):
    tekst = input("Unesite tekst: ")
    zamenjeni_tekst = ""

    for i in tekst:
        if i == x:
            zamenjeni_tekst += y
            continue
        zamenjeni_tekst += i

    return zamenjeni_tekst

print(zameni_slova("a", "z"))
