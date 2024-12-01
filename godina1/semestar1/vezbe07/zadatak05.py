import os; os.system("cls")

def obrisi_element(list_of_numbers, n):
    while n in list_of_numbers:
        list_of_numbers.remove(n)
    return list_of_numbers

print(obrisi_element([1, 5, 3, 9, 4, 5], 5))
