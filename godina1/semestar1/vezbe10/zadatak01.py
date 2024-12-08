import os; os.system("cls")

with open("studenti.txt", mode = "r", encoding = "UTF-8") as file:
    file_content = file.read()

print(file_content)
