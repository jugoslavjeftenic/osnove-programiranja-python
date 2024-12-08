import os; os.system("cls")

with open("studenti.txt", mode = "r", encoding = "UTF-8") as file:
    for line in file:
        student = line.strip().split(", ")
        if "Jovanovic" in student[1]:
            print("Student sa prezimenom", student[1], "ima bodova:", int(student[2]))
