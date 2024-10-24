import os; os.system("cls")

def prosek():
    print("Info. Za prekid programa upisite negativan ceo broj.")
    suma = 0
    brojac = 0
    while True:
        try:
            broj = int(input("Unesite pozitivan ceo broj: "))
            if broj < 0:
                break
            if broj == 0:
                continue
        except ValueError:
            print("Greska. Niste upisali validan ceo broj!")
            continue
        suma += broj
        brojac += 1
    try:
        return suma / brojac
    except ZeroDivisionError:
        return "Suma je nula. Nije moguce izracunati prosek."

print(prosek())