from os import system; system("cls")

# Napisati funkciju je_savrsen_broj koja prima broj n i vraća True ako je broj savršen
# (jednak zbiru svojih pravih delilaca), ili False u suprotnom.
# Na primer, je_savrsen_broj(28) treba da vrati True.

def je_savrsen_broj(n):
    zbir_delilaca = 0
    for i in range(1, n//2+1):
        if n % i == 0:
            zbir_delilaca += i
    
    return zbir_delilaca == n

print("Broj je savrsen:", je_savrsen_broj(28))
