import os; os.system("cls")

def podeli(a, b):
    try:
        print(a / b)
    except ZeroDivisionError:
        print("Dijeljenje nulom nije moguce.")

podeli(8, 4)
