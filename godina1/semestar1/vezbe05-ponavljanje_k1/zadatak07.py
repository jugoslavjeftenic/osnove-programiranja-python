from os import system; system("cls")

# Napisati funkciju broj_velikih_slova koja prima string i vraća broj velikih slova u stringu.
# Na primer, broj_velikih_slova("Kolokvijum Je Težak") treba da vrati 3.

def broj_velikih_slova(text):

    return sum(1 for c in text if c.isupper())

print("Broj velikih slova:", broj_velikih_slova("Kolokvijum Je Tezak"))
print("Broj velikih slova:", broj_velikih_slova("Kolokvijum nije Tezak Ako si Ucio"))
