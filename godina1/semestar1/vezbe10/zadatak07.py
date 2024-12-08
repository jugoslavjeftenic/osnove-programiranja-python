import os; os.system("cls")

is_streber = False
with open("bodovi.txt", mode = "r", encoding = "UTF-8") as file:
    for line in file:
        if int(line.strip()) == 100:
            is_streber = True
            break

if is_streber:
    print("Postoji student sa 100 poena.")
