import os; os.system("cls")

file = open("studenti.csv", mode = "r", encoding = "UTF-8")
content = file.readlines()
file.close()

students = []
points = 0
for element in content:
    students.append(element.strip().split(","))

for student in students:
    points += int(student[2])

print(students)
print(points)
