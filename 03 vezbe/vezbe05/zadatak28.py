from os import system; system("cls")

# Napisati funkciju broj_cifara koja prima prirodan broj n i vraća broj cifara tog broja.
# Na primer, poziv broj_cifara(402000) treba da vrati 6.

def broj_cifara(n):
    counter = 0
    while n > 0:
        n //= 10
        counter += 1
    return counter

print("Broj cifara:", broj_cifara(402000))
