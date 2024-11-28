import os; os.system("cls")

def faktorijel(n):
    # n = int(input("Upisite broj n koji je veci od 0: "))
    proizvod = 1
    for i in range(1, n + 1):
        proizvod *= i
    return proizvod

print(faktorijel(int(input("Upisite broj n koji je veci od 0: "))))
print(faktorijel(4))
print(faktorijel(10))
print(faktorijel())
