import os; os.system("cls")
# F(n) = F(n-1) + F(n-2)

def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

n = int(input("Unesite indeks za Fibonacijev broj: "))
print("Fibonacijev broj za indeks", n, "je", fib(n))
