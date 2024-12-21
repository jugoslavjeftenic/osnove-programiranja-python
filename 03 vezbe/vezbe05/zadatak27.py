from os import system; system("cls")

# Napisati funkciju zameni_reci koja prima dve reči, stara i nova.
# Funkcija treba da od korisnika zatraži neki string, a zatim da u stringu zameni svaku pojavu reči stara rečju nova.
# Povratna vrednost je izmenjeni string.

def zameni_reci(old_string, new_string):
    # input_text = input("Upisite recenicu: ")
    input_text = "Vazduh trepti kao da nebo gori."
    return input_text.replace(old_string, new_string)

print(zameni_reci("trepti", "plamti"))
