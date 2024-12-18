import os; os.system("cls")
from math import floor

def zaokruzi_na_veci(n_list):
    return [floor(n) for n in n_list]

print(zaokruzi_na_veci([5.6, 0.6, -2.2]))
