import os; os.system("cls")

bodovi = []
with open("studenti.txt", mode = "r", encoding = "UTF-8") as input_file:
    for line in input_file:
        bodovi.append(line.strip().split(", ")[2] + "\n")

with open("bodovi.txt", mode = "w", encoding = "UTF-8") as output_file:
    output_file.writelines(bodovi)
