import os; os.system("cls")

def napravi_listu(pocetak, kraj):
    ret_val = []
    for i in range(pocetak, kraj+1):
        ret_val.append(i)
    return ret_val

lista = napravi_listu(2, 5)
print(lista[0])
print(lista[-1])
