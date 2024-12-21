from os import system; system("cls")

with open("studenti.csv",mode="r",encoding="UTF-8") as file:
    file.readline()
    students = []
    female_count = 0
    male_count = 0

    for line in file:
        student = line.strip().split(",")
        gender = student[2].strip().lower()
        if gender == "ženski":
            female_count += 1
        else:
            male_count += 1

    if female_count > male_count: print("U fajlu ima vise zenskih studenata.")
    elif female_count < male_count: print("U fajlu ima vise muskih studenata.")
    else: print("U fajlu je jednako muskih i zenskih studenata.")
