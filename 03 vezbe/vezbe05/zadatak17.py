import os; os.system("cls")

# Funkcija: zbir_cifara Napisati funkciju zbir_cifara koja kao parametar prima cijeli broj n i
# vraća zbir svih cifara tog broja. Na primjer, poziv zbir_cifara(1234) treba da vrati 10.

def zbir_cifara(n):
    suma = 0
    for i in str(n):
        suma += int(i)
    return suma

print(zbir_cifara(1234))
