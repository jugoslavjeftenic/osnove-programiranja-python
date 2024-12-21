from os import system; system("cls")

# Napisati funkciju najduza_rec koja od korisnika traži da unese tekst i vraća najdužu reč iz tog teksta.
# Na primer, za unos „Python je programski jezik“, funkcija treba da vrati „programski“.

def najduza_rec():
    # input_text = input("Upisite recenicu: ")
    input_text = "Python je programski jezik"
    return max(input_text.split(), key = len)

print("Najduza rec je:", najduza_rec())
