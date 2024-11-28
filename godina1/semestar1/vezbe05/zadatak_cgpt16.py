import os; os.system("cls")

# Funkcija: broj_savrsenih Napisati funkciju broj_savrsenih koja prima dva prirodna broja m i n i
# vraća broj savršenih brojeva u intervalu [m, n].
# Napomena: Broj je savršen ako je jednak zbiru svojih pravih djelilaca.

def da_li_je_savrsen(n):
    suma = 0
    for i in range(1, n):
        if n % i == 0:
            suma += i
    return n == suma

def broj_savrsenih(m, n):
    brojac = 0
    for i in range(m, n + 1):
        if da_li_je_savrsen(i):
            print(i, "je savrsen broj")
            brojac += 1
    return brojac

print("Interval sadrzi ukupno savrsenih brojeva:", broj_savrsenih(1, 1000))
