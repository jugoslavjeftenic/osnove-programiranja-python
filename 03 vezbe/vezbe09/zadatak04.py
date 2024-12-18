import os; os.system("cls")

file = open("brojevi.txt", mode = "r", encoding = "UTF-8")
content = file.read().split("\n")
file.close()

sum = 0
for i in content:
    try:
        sum += int(i)
    except:
        print("NaN")

file = open("brojevi_sum.txt", mode = "w", encoding = "UTF-8")
file.write(str(sum))
file.close()
