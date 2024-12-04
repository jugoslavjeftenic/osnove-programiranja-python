import os; os.system("cls")

file = open("predmeti.txt", mode = "r", encoding = "UTF-8")
content = file.read()
file.close()

file = open("lowercase.txt", mode = "w", encoding = "UTF-8")
file.write(content.lower())
file.close()
