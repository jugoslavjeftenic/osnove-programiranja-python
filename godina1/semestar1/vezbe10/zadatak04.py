import os; os.system("cls")

with open("studenti.txt", mode = "r", encoding = "UTF-8") as file:
    for line in file:
        print(line.strip().split(", ")[1])
