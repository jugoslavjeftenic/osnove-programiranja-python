import os; os.system("cls")

with open("studenti.txt", mode = "r", encoding = "UTF-8") as file:
    file_content = file.readlines()

print("Broj linija u datoteci je:", len(file_content))
