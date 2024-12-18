import os; os.system("cls")

def faktorijel(n):
    f = 1
    for i in range(1, n+1):
        f *= i
        print(i, f)
    return f

print("Faktorijel je", faktorijel(5))
