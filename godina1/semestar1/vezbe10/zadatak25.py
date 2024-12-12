import os; os.system("cls")

def ima_li_duplikata(list):
    return len(list) != len(set(list))

print("Da li ima duplikata?", ima_li_duplikata([5, 3, 5, 6]))
print("Da li ima duplikata?", ima_li_duplikata([5, 7, 9]))
