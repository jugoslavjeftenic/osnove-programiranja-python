import os; os.system("cls")

def nadji_dva_najveca(n_list):
    if len(n_list) < 2:
        print("Lista nema dovoljno elemenata.")
        return ()
    
    n_list.sort()
    return (n_list[-2], n_list[-1])

print("Najveci brojevi u listi su:", nadji_dva_najveca([5, 3, 7, 0, 6]))
