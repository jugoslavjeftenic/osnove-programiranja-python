from os import system; system("cls")
from json import load

matches = []
with open("utakmice.json", mode="r", encoding="UTF-8") as file:
    matches = load(file)

# Odrediti koliko utakmica je odigrano.
print(f"Odigrano je {len(matches)} utakmica.")

# Odrediti prosjecnu duzinu utakmica.
duration = sum(match["duration"] for match in matches)
print(f"Prosecna duzina utakmice je {duration / len(matches):.2f} minuta.")

# Napraviti listu koja ce sadrzati samo nazive timova koji su postigli bar jedan go.
teams_with_scores = {
    match[team]["name"]
    for match in matches
    for team in ["team1", "team2"]
    if match[team]["score"] > 0
}
print(f"Timovi koji su postigli bar jedan go: {", ".join(teams_with_scores)}.")

# Ispisati imena timova koji su ukupno imali bar 3 zuta kartona
teams_with_yellow_cards = {}
for match in matches:
    for team in ["team1", "team2"]:
        if match[team]["yellow_cards"] > 0:
            if match[team]["name"] in teams_with_yellow_cards:
                teams_with_yellow_cards[match[team]["name"]] += match[team]["yellow_cards"]
            else:
                teams_with_yellow_cards[match[team]["name"]] = match[team]["yellow_cards"]
teams_with_yellow_cards = [team for team, cards in teams_with_yellow_cards.items() if cards >= 3]
print(f"Timovi koji su ukupno imali bar 3 zuta kartona: {", ".join(map(str, teams_with_yellow_cards))}.")
