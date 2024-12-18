import os; os.system("cls")

def iscrtaj(n):
    print("*" * n)
    if n == 0:
        return
    iscrtaj(n - 1)

iscrtaj(5)
