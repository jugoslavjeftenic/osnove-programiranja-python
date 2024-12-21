from os import system; system("cls")

def razdvoj_naslov():
    naslov = input("Upisite naslov: ")
    n = int(input("Upisite prirodan broj: "))
    return (" " * n).join(naslov)

print(razdvoj_naslov())
