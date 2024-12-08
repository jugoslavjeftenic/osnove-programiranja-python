import os; os.system("cls")

with open("bodovi.txt", mode = "r", encoding = "UTF-8") as file:
    file_content = file.readlines()

prosek = 0
for poeni in file_content:
    prosek += int(poeni.strip())
prosek = prosek / len(file_content)

print("Studenti su u proseku imali poena:", prosek)
