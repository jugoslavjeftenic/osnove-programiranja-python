import os; os.system("cls")

def ispis():
    try:
        n = int(input("Unesite prirodan broj: "))
        if n < 1: raise ValueError

        for i in range(1, n):
            print(i)
    except ValueError:
        print("Niste uneli prirodan broj.")
    
ispis()
