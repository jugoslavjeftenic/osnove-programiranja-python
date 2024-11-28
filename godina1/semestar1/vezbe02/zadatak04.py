import os; os.system("cls")     # brise sadrzaj terminala

poeni_k1 = 23
poeni_k2 = 14
poeni_ispit = 21
poeni = poeni_k1 + poeni_k2 + poeni_ispit

if poeni_k1 >= 15 and poeni_k2 >= 15 and poeni >= 51:
    print("Ispit je polozen.")
    if   poeni > 90: print("Ocena je 10.")
    elif poeni > 80: print("Ocena je 9.")
    elif poeni > 70: print("Ocena je 8.")
    elif poeni > 60: print("Ocena je 7.")
    elif poeni > 50: print("Ocena je 6.")
