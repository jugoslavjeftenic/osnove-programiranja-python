import os; os.system("cls")
from random import randint

def baci_novcic():
    # novcic = randint(0, 1)
    # if novcic == 0: print("Pismo")
    # else: print("Glava")
    print("Pismo" if randint(0, 1) == 0 else "Glava")

baci_novcic()
