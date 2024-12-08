import os; os.system("cls")
from math import sqrt

def korenuj():
    n = input("Unesite pozitivan broj: ")
    try:
        if not n.isdigit(): raise ValueError("Uneseni broj nije validan.")

        n = float(n)
        if n <= 0: raise ValueError("Uneseni broj mora biti pozitivan.")

        return sqrt(n)

    except ValueError as e:
        return e
    
print(korenuj())
