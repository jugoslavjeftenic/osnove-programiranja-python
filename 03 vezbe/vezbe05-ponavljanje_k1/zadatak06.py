from os import system; system("cls")

# Napisati funkciju obrni_reci koja od korisnika traži da unese rečenicu,
# a zatim vraća novu rečenicu u kojoj su sve reči obrnutim redosledom.
# Na primer, za unos „Python je super“, funkcija treba da vrati „super je Python“.

def obrni_reci():
    # input_text = input("Unesite recenicu: ")
    input_text = "Python je super"

    text_list = input_text.split()
    # text_list.reverse()
    return " ".join(text_list[::-1])

print(obrni_reci())
