import os; os.system("cls")

def broj_malih_slova(niz_karaktera):
    # velika_slova = (
    #     list(range(65, 91)) +  # Velika slova engleskog alfabeta (A-Z)
    #     list(range(192, 215)) +  # Velika slova proširenog latiničnog skupa
    #     list(range(216, 223)) +  # Nastavak velikih slova latiničnog skupa
    #     [268, 262, 272, 352, 381]  # Pojedinačne vrednosti za velika slova srpske latinice
    # )
    mala_slova = (
        list(range(97, 123)) +  # Mala slova engleskog alfabeta (a-z)
        list(range(224, 247)) +  # Mala slova proširenog latiničnog skupa
        list(range(248, 255)) +  # Nastavak malih slova latiničnog skupa
        [269, 263, 273, 353, 382]  # Pojedinačne vrednosti za mala slova srpske latinice
    )
    ret_val = 0

    for karakter in niz_karaktera:
        if ord(karakter) in mala_slova:
            ret_val += 1
    
    return ret_val

niz_karaktera = "PerA pErIc"
print("U nizu karaktera: \"" + niz_karaktera + "\" ima ukupno", broj_malih_slova(niz_karaktera), "malih slova.")
