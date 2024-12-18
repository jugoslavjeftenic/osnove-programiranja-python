import os; os.system("cls")

# Funkcija: ponavljajuca_rijec Napisati funkciju ponavljajuca_rijec koja prima string koji
# sadrži više riječi i vraća riječ koja se najčešće ponavlja u stringu.
# Ako postoji više riječi koje se najčešće ponavljaju, funkcija vraća prvu koja je naišla.

def ponavljajuca_rijec(tekst):
    # lista_reci = tekst.lower().replace(".", "").split()

    lista_reci = []
    rec_za_listu = ""
    for i in range(0, len(tekst)):
        if tekst[i] == " " or  tekst[i] == ".":
            lista_reci.append(rec_za_listu)
            rec_za_listu = ""
        else:
            rec_za_listu += tekst[i]

    # print(lista_reci)

    recnik_reci = {}

    for rec in lista_reci:
        if rec in recnik_reci:
            recnik_reci[rec] += 1
        else:
            recnik_reci[rec] = 1

    # print(recnik_reci)

    najcesca_rec = ""
    brojac_reci = 0
    for rec in recnik_reci:    
        if recnik_reci[rec] > brojac_reci:
            najcesca_rec = rec
            brojac_reci = recnik_reci[rec]
    
    print("Rec: \"" + najcesca_rec + "\" se ponovila", brojac_reci, "puta.")

ponavljajuca_rijec("Ovaj tekst ima vise reci i ima dve reci koje se ponavljaju. Sta reci a ne ponoviti a da je u recniku reci.")
