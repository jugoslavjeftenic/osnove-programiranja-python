import os; os.system("cls")

def is_savrsen(n):
    suma = 0
    for i in range(1, n):
        if n % i == 0:
            suma += i
    return n == suma

def ispisi_savrsen(m, n):
    for i in range(m, n + 1):
        if is_savrsen(i):
            print("Savrsen", i)

print(ispisi_savrsen(0, 1000))
