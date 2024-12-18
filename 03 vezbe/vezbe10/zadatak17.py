import os; os.system("cls")

def prebroj(n_tuple):
    try:
        n = int(input("Unesite broj: "))
        return n_tuple.count(n)
    except ValueError:
        print("Niste uneli ispravan broj.")

print(f"Trazeni broj se pojavljuje {prebroj((6, 4, 6, 3))} puta.")
