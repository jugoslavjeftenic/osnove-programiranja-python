import os; os.system("cls")

# Napisati funkciju faktorijal koja kao parametar prima prirodan broj n, a vraća njegov faktorijal (n!).
# Npr. poziv faktorijal(5) treba da vrati 120.

def faktorijal(n):
    faktorijal = 1
    for i in range(1, n + 1):
        faktorijal *= i
    
    print(str(n) + "! =", faktorijal)

faktorijal(3)
