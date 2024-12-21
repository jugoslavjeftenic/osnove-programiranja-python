import os; os.system("cls")

# Napisati funkciju ispisi_stepene koja prima dva prirodna broja m i n.
# Funkcija treba da ispiše sve brojeve koji su stepen broja 2 u intervalu [m, n] (npr. 1, 2, 4, 8, 16,...).

def ispisi_stepene(m, n):
    for i in range(m, n + 1):
        print("2 na", i, "je", 2 ** i)

ispisi_stepene(0, 10)
