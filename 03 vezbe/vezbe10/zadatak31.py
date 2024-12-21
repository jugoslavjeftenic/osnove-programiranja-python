from os import system; system("cls")

def prevedi(sentence):
    rjecnik = {
        "Ja":"I",
        "volim":"love",
        "igrati":"play",
        "nebo":"sky",
        "programiranje":"programming"
    }
    ret_val = []

    words = sentence.split(" ")
    for word in words:
        if word in rjecnik:
            ret_val.append(rjecnik[word])
        else: return "Zao nam je, data recenica ne postoji u nasem rjecniku."

    return " ".join(ret_val)

print(prevedi("Ja volim programiranje"))
print(prevedi("Vazduh trepti kao da nebo gori"))
