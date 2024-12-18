import os; os.system("cls")

file = open("predmeti.txt", mode = "r", encoding = "UTF-8")
content = file.read()
file.close()

print(content)
