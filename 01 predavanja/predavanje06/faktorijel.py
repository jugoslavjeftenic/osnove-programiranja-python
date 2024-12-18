import os; os.system("cls")

def faktorijel(n):
    if n == 0:
        return 1
    else:
        print(n)
        return n * faktorijel(n - 1)

print("Rezultat je", faktorijel(4))
