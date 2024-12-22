from os import system; system("cls")
import json

with open("studenti.csv", mode="r", encoding="UTF-8") as file:
    studenti = [
        {"ime": ime,
         "prezime": prezime,
         "ocene": list(map(int, ocene.split(";"))),
         "zaposlen": zaposlen == True}
        for line in file
        for ime, prezime, ocene, zaposlen in [line.strip().split(",")]
    ]

print(studenti)

with open("studenti1.json", mode="w", encoding="UTF-8") as file:
    json.dump(studenti, file, indent=4)

with open("studenti1.json", mode="r", encoding="UTF-8") as file:
    print(json.load(file))
