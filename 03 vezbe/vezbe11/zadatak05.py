from os import system; system("cls")
from json import dump, load

matches_string = \
    "tim1-tim2-rezultat-odnos žutih kartona-trajanje\n" \
    "Japan-Belgija-2:0-2:2-103\n" \
    "Engleska-Švajcarska-3:5-1:2-95\n" \
    "Engleska-Senegal-1:6-1:1-92\n" \
    "Belgija-Švajcarska-0:6-0:1-101\n" \
    "Japan-Katar-1:0-0:1-99\n" \
    "Katar-Senegal-6:0-1:3-90"

matches = matches_string.split("\n")
del matches[0]

for i in range(0, len(matches)):
    match = matches[i].split("-")
    score = list(map(int, match[2].split(":")))
    yellow_cards = list(map(int, match[3].split(":")))

    matches[i] = {"duration":int(match[4]), \
        "team1":{"name":match[0], "score":score[0], "yellow_cards":yellow_cards[0]}, \
        "team2":{"name":match[1], "score":score[1], "yellow_cards":yellow_cards[1]}}

with open("utakmice.json", mode="w", encoding="UTF-8") as file:
    dump(matches, file, indent=4, ensure_ascii=False)

with open("utakmice.json", mode="r", encoding="UTF-8") as file:
    print(load(file))
