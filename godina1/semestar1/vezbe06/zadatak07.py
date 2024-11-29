import os; os.system("cls")

def suma_brojeva(n):
    sum = 0
    for i in range(n + 1):
        sum += i
    return sum

def suma_brojeva_rekurzivno(n):
    if n == 1:
        return 1
    return n + suma_brojeva_rekurzivno(n - 1)

print(suma_brojeva(3))
print(suma_brojeva_rekurzivno(3))
