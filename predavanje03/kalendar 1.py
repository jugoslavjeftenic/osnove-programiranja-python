# n = 365 + g//4 - (g//100 - g//400)
import os; os.system("cls")     # brise sadrzaj terminala

g = int(input("Unesite godinu: "))
n = 365 * g + g // 4 - (g // 100 - g // 400)
print(n)
