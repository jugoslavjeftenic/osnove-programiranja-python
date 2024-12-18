import os; os.system("cls")

countries = {"Rusija":16377742, "Kanada":9093507, "Kina":9569901, "SAD":9158960}

while True:
    country = input("Upisite naziv trazene drzave: ")
    if country == "":
        break
    try:
        print("Povrsina drzave", country, "je", countries[country], "km2.")
    except KeyError:
        print("Nazalost nemamo informacija o toj drzavi.")
