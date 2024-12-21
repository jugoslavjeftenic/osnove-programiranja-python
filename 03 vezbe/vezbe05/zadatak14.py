import os; os.system("cls")

# Napisati funkciju ispisi_armstrong koja prima dva prirodna broja m i n.
# Funkcija treba da ispiše sve Armstrongove brojeve u intervalu [m, n].
# (Broj je Armstrongov ako je jednak zbiru svojih cifara podignutih na n-ti stepen,
# gde je n broj cifara tog broja. Npr. 153 = 1^3 + 5^3 + 3^3).

def is_armstrong(n):
    zbir = 0
    for i in str(n):
        zbir += int(i) ** len(str(n))
    return n == zbir

def ispisi_armstrong(m, n):
    for i in range(m, n + 1):
        if is_armstrong(i):
            print(i)

ispisi_armstrong(1, 2000)
