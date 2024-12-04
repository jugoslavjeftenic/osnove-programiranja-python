import os; os.system("cls")

file = open("studenti.csv", mode = "r", encoding = "UTF-8")
content = file.readlines()
file.close()

students = []
for element in content:
    students.append(element.strip().split(","))

print(students)
