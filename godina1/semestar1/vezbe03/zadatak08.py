import os; os.system("cls")

n = int(input("Upisite broj n koji je veci od 0: "))

brojac = 1
while brojac <= n:
    print(str(brojac) * brojac)
    brojac += 1
