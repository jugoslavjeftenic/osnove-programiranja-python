import os; os.system("cls")

with open("studenti.txt", mode = "r", encoding = "UTF-8") as file:
    file_content = file.read()

print("Broj ponavljanja reci \"Marko\" u datoteci je:", file_content.count("Marko,"))
