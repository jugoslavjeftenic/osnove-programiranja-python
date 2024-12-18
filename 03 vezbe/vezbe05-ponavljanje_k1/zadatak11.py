import os; os.system("cls")

def nadji_najveci(m = 10, n = 99):
    for i in range(n, m-1, -1):
        poslednja_cifra = i % 10

        if poslednja_cifra == 0: continue
        if i % poslednja_cifra == 0:
            print("Najveci broj deljiv sa svojom poslednjom cifrom je:", i)
            break

nadji_najveci(10, 30)
