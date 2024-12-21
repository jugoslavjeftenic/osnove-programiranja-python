import os; os.system("cls")

# Napiši funkciju koja pronalazi najmanji broj u opsegu [m, n] koji je deljiv svojom prvom cifrom.
# Ako se funkciji ne proslede argumenti, pretražuje brojeve od 10 do 99.Na primer, za opseg [20, 50],
# brojevi deljivi svojom prvom cifrom su: 22, 24, 33, 44, a najmanji je 22.

def nadji_najmanji(m = 10, n = 99):
    for i in range(m, n+1):
        prva_cifra = i
        while prva_cifra > 10: prva_cifra //= 10

        if i < 1 or prva_cifra == 0: continue
        if i % prva_cifra == 0:
            print("Najmanji broj deljiv sa svojom prvom cifrom je:", i)
            break

nadji_najmanji(7, 50)
