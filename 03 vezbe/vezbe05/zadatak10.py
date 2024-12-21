import os; os.system("cls")

# Napisati funkciju iscrtaj_pravougaonik koja prima dva prirodna broja visina i sirina i jedan karakter c.
# Funkcija treba da iscrta pravougaonik zadatih dimenzija koristeći karakter c.
# Na primer, ako se unese visina=3, sirina=5 i c="*", funkcija treba da iscrta:
# *****
# *****
# *****

def iscrtaj_pravougaonik(sirina, visina, karakter):
    # for x in range(0, visina):
    #     print(karakter * sirina)

    # red_teksta = ""
    # for i in range(0, sirina):
    #     red_teksta += karakter
    # for i in range(0, visina):
    #     print(red_teksta)

    for i in range(0, visina):
        for o in range(0, sirina):
            print(karakter, end="")
        print()

iscrtaj_pravougaonik(5, 3, "#")
