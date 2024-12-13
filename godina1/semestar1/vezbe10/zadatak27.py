import os; os.system("cls")
from random import randint

def odaberi_slucajan_broj(n_list):
    print("Nasumicno izabran element:", n_list[randint(0, len(n_list)-1)])

odaberi_slucajan_broj([10, 11, 12, 13, 14, 15])
