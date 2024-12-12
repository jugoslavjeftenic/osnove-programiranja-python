import os; os.system("cls")

def ispis(n_tuple):
    # print(", ".join(str(n) for n in n_tuple))
    print(", ".join(map(str, n_tuple)))

ispis((5, 6, 7, 2))
