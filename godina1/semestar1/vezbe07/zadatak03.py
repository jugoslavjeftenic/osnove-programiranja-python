import os; os.system("cls")

def kreiraj_recnik():
    ret_val = {}
    ret_val["ime"] = input("Unesite ime: ")
    ret_val["prezime"] = input("Unesite prezime: ")
    try:
        ret_val["godine"] = int(input("Unesite godine: "))
    except ValueError:
        print("Godine starosti nisu ispravan broj.")
        ret_val["godine"] = 0
    return ret_val

person_1 = kreiraj_recnik()
person_2 = kreiraj_recnik()

for i in person_1.keys():
    print(i)

for i in person_2.values():
    print(i)
