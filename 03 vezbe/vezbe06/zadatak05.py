import os; os.system("cls")

def sumiraj():
    sum = 0
    try:
        while True:
            n = int(input("Unesite broj: "))
            sum += n
    finally:
        return sum

print("Suma unetih brojeva:", sumiraj())
