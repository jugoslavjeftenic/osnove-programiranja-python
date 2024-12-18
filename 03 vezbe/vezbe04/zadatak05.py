import os; os.system("cls")

def izracunaj_ocenu(broj_bodova = 0):
    if broj_bodova > 90:
        return 10
    if broj_bodova > 80:
        return 9
    if broj_bodova > 70:
        return 8
    if broj_bodova > 60:
        return 7
    if broj_bodova > 50:
        return 6
    else:
        return 5

ocena = 5
ocena = izracunaj_ocenu()
print(ocena)
