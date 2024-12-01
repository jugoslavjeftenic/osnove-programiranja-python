import os; os.system("cls")

def nadji_najveci(list_of_numbers):
    list_of_numbers.sort(reverse = True)
    return list_of_numbers[0]

print(nadji_najveci([1, 5, 3, 9, 4]))
