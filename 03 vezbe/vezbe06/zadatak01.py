import os; os.system("cls")

def faktorijel_rekurzivno(n):
    if n == 0:
        return 1
    return n * faktorijel_rekurzivno(n - 1)

print(faktorijel_rekurzivno(5))
