from os import system; system("cls")

# Napisati funkciju je_palindrom koja prima string i vraća True ako je string palindrom (čita se isto s leva na desno i s desna na levo),
# ili False u suprotnom. Na primer, je_palindrom("radar") treba da vrati True.

def je_palindrom(s):
    return s == s[::-1]

print("Da li je palindrom:", je_palindrom("radar"))
