# n = 365 + g//4 - (g//100 - g//400)
import os; os.system("cls")     # brise sadrzaj terminala

g = int(input("Unesite godinu 1: "))
n = 365 * g + g // 4 - (g // 100 - g // 400)

g = int(input("Unesite godinu 2: "))
m = 365 * g + g // 4 - (g // 100 - g // 400)

print(n - m)
