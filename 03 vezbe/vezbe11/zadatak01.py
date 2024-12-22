from os import system; system("cls")
import json

studenti_to_write = [
    {"270270":"Marko Markovic"},
    {"270271":"Janko Jankovic"},
    {"270272":"Pera Peric"}
]

with open("studenti2.json", mode="w", encoding="UTF-8") as file:
    json.dump(studenti_to_write, file, indent=4)

with open("studenti2.json", mode="r", encoding="UTF-8") as file:
    studenti_to_read = json.load(file)

print(studenti_to_read)
print(studenti_to_read[1]["270271"])
for student in studenti_to_read:
    if "270271" in student:
        print(student)
