import os; os.system("cls")

# Napisati funkciju ispisi_prim koja kao parametar prima dva prirodna broja m i n,
# i ispisuje sve proste brojeve u intervalu [m, n].

def is_prim(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def ispisi_prim(m, n):
    for i in range(m, n + 1):
        if is_prim(i):
            print("Broj", i, "je primaran broj.")

ispisi_prim(1, 11)
