import os; os.system("cls")

# Napisati funkciju izbaci_samoglasnike koja traži od korisnika da unese string,
# a zatim uklanja sve samoglasnike (a, e, i, o, u) iz tog stringa. Funkcija vraća rezultat.

def izbaci_samoglasnike():
    tekst = input("Unesi tekst: ")
    ret_val = ""
    for i in tekst:
        match i:
            case "a" | "e" | "i" | "o" | "u":
                continue
            case _:
                ret_val += i
    return ret_val

print(izbaci_samoglasnike())
