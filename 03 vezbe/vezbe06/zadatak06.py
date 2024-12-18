import os; os.system("cls")

def sumiraj():
    try:
        a = int(input("Unesite broj a: "))
        b = int(input("Unesite broj b: "))
        return a + b
    except ValueError:
        print("Unetu vrednost nije moguce konvertovati u broj.")

print("Suma unetih brojeva:", sumiraj())
