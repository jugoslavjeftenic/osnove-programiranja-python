from os import system; system("cls")

# Napisati funkciju broj_vokala koja prima string i vraća broj vokala (a, e, i, o, u) u stringu.
# Na primer, broj_vokala("Kolokvijum") treba da vrati 4.

def broj_vokala(text):
    vokali = {"a", "e", "i", "o", "u"}
    return sum(1 for c in text if c.lower() in vokali)

print("Broj vokala u tekstu:", broj_vokala("KolokvIjum"))
