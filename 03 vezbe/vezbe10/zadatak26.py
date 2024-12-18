import os; os.system("cls")
from random import randint

def generisi_nasumican_broj():
    a = int(input("Upisite prvi broj: "))
    b = int(input("Upisite drugi broj: "))
    print("Nasumican broj je:", randint(a, b))

generisi_nasumican_broj()
