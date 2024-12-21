import os; os.system("cls")

# Napiši funkciju koja pronalazi najveći broj u opsegu [m, n] koji ima zbir svojih cifara deljiv sa 3.
# Ako se funkciji ne proslede argumenti, pretražuje brojeve od 1 do 100.
# Na primer, za opseg [10, 20], brojevi su: 12, 15, 18, a najveći je 18.

def najveci_broj(m = 1, n = 100):
    for i in range(n, m-1, -1):
        deljenik = 0
        if i > 0 and i < 10: deljenik = i
        if i == 10: deljenik = 1

        x = i
        while x > 10:
            deljenik += x % 10
            x //= 10
            if x < 10: deljenik += x
        
        if deljenik % 3 == 0:
            print("Najveci broj ciji zbir cifara je deljiv sa 3 jeste:", i)
            break

najveci_broj(1, 98)
