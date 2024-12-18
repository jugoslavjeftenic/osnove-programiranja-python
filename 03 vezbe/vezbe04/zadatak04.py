import os; os.system("cls")

def prva_rec():
    recenica = input("Upisite proizvoljnu recenicu: ")
    return recenica.split()[0]

print(prva_rec())
