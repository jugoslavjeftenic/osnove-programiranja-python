import os; os.system("cls")
from math import ceil

def rounding():
    try:
        n = float(input("Unesite decimalan broj: "))
        print("Uneti broj zaokruzen na vece:", ceil(n))
    except ValueError:
        print("Niste upisali decimalan broj.")

rounding()
