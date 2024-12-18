import os; os.system("cls")

def saberi_vrijednosti(dict):

    dict_sum = 0
    try:
        for vrijednost in dict.values():
            dict_sum += vrijednost
    except:
        return None
    
    return dict_sum

vrijednosti = {1:5, 2:10}
# vrijednosti = {1:5, 2:10, 3:"re"}
print(saberi_vrijednosti(vrijednosti))
