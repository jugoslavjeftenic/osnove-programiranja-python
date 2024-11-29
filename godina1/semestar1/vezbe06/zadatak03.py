import os; os.system("cls")

def fib(n):
    # F(n) = F(n-1) + F(n-2)
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

print(fib(6))
print(fib(9))
