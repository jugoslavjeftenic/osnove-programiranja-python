import os; os.system("cls")

file = open("new_file.txt", mode = "w", encoding = "UTF-8")
file.write("10")
file.write("\n")
file.write("Novi string")
file.write("\n")
file.write("True")
file.write("\n")
file.write("14.3")
file.close()