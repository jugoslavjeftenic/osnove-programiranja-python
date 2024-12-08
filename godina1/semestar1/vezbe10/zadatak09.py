import os; os.system("cls")

has_10grade = 0
with open("bodovi.txt", mode = "r", encoding = "UTF-8") as file:
    for line in file:
        line = line.strip()
        if line.isdigit() and int(line) > 90:
            has_10grade += 1

print("Broj studenata sa ocenom 10 je:", has_10grade)
