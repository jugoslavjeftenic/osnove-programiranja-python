import os; os.system("cls")

# Funkcija: iscrtaj_trokut Napisati funkciju iscrtaj_trokut koja prima jedan cijeli broj n.
# Funkcija treba da iscrta pravougli trokut visine n, koristeći karakter *.
# Na primjer, za n = 4, iscrtava:
# *
# **
# ***
# ****

def iscrtaj_trokut(n):
    for i in range(0, n):
        print("*" * (i + 1))

iscrtaj_trokut(4)
