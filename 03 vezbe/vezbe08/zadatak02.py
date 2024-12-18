import os; os.system("cls")
import math

def koliko_farbe(r):
    p = r**2 * math.pi
    return math.ceil(p)

print("Zeno, kupi", koliko_farbe(7), "kutija farbe.")
