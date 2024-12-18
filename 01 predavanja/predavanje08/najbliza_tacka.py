import os; os.system("cls")
import math

def euklid(x, y):
    return math.sqrt((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2)

tacke = [[-1,3],[-1,-1],[1,1],[2,0.5],[2,-1],[3,3],[4,2],[4,-0.5]]
zadana_tacka = [2,2]

najbliza_tacka = tacke[0]
mind = euklid(zadana_tacka, najbliza_tacka)

for i in range(1,len(tacke)):
    d = euklid(zadana_tacka, tacke[i])
    if d < mind:
        najbliza_tacka = tacke[i]
        mind = d

print("Najbliza tacka tacki", zadana_tacka, "je", najbliza_tacka, "udaljena", mind)
