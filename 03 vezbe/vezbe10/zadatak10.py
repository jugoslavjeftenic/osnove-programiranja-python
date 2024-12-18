import os; os.system("cls")

top_student = ("", "", 0)
studenti = []
with open("studenti.txt", mode = "r", encoding = "UTF-8") as file:
    for line in file:
        ime, prezime, bodovi = line.strip().split(", ")
        bodovi = int(bodovi)
        studenti.append([ime, prezime, bodovi])
        if bodovi > top_student[2]:
            top_student = [ime, prezime, bodovi]

print("Student sa najvise bodova je:", top_student[0], top_student[1])
