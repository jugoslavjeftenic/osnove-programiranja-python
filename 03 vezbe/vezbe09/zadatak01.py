import os; os.system("cls")

file = open("predmeti.txt", mode = "r", encoding = "UTF-8")

content = file.read()
file.seek(0)
print(content)
print(type(content))

print("-----------------------")
content = file.readlines()
file.seek(0)
print(content)
print(type(content))

print("-----------------------")
content1 = file.readline()
content2 = file.readline()
print(content1.strip())
print(content2.strip())
print(type(content1))
print(type(content2))

file.close()
