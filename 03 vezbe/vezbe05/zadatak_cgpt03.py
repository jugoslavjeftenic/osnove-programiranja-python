import os; os.system("cls")

# Napisati funkciju saberi_neparne koja prima dva prirodna broja, m i n.
# Funkcija vraća sumu svih neparnih brojeva u intervalu [m, n] (uključujući m i n).

def saberi_neparne(m, n):
    suma = 0
    for i in range(m, n + 1):
        if i % 2 != 0:
            suma += i
    
    return suma

print(saberi_neparne(1, 20))
