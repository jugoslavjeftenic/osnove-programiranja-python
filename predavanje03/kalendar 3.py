import os; os.system("cls")     # brise sadrzaj terminala

print("Unesite prvi datum")
dan1 = int(input("Dan: "))
mesec1 = int(input("Mesec: "))
godina1 = int(input("Godina: "))

print("Unesite drugi datum")
dan2 = int(input("Dan: "))
mesec2 = int(input("Mesec: "))
godina2 = int(input("Godina: "))

m1 = (mesec1 + 9) % 12
m2 = (mesec2 + 9) % 12

g1 = godina1 - m1 // 10
g2 = godina2 - m2 // 10

n1 = 365 * g1 + g1 // 4 - g1 // 100 + g1 // 400 + (m1 * 306 + 5) // 10 + dan1 - 1
n2 = 365 * g2 + g2 // 4 - g2 // 100 + g2 // 400 + (m2 * 306 + 5) // 10 + dan2 - 1

n = n2 - n1
print("Broj dana izmedju", dan1, mesec1, godina1, "i", dan2, mesec2, godina2, "je", n)
