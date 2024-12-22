from os import system; system("cls")
import json

with open("studenti2.json", mode="r", encoding="UTF-8") as file:
    studenti = json.load(file)

studenti.append({"270273":"Jugoslav Jeftenic"})
studenti.append({"270274":"Mitar Miric"})

with open("studenti3.json", mode="w", encoding="UTF-8") as file:
    json.dump(studenti, file, indent=4)
