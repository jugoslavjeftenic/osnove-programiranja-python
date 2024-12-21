import os; os.system("cls")

# Napisati funkciju zameni_slova koja prima dva karaktera, x i y.
# Funkcija traži od korisnika da unese rečenicu, a zatim zameni svaki karakter x sa y u toj rečenici.
# Funkcija vraća izmenjenu rečenicu.

def zameni_slova(x, y):
    tekst = input("Unesite recenicu: ")
    ret_val = ""

    for i in tekst:
        if i == x:
            ret_val += y
            continue
        ret_val += i
    return ret_val

print(zameni_slova("a", "az"))
