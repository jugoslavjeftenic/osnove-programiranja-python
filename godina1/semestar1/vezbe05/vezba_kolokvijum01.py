import os; os.system("cls")

def zamijeni_karaktere(x, y):
    ret_val = ""
    tekst = input("Unesite neki tekst: ")

    # for karakter in tekst:
    #     if karakter == x:
    #         ret_val += y
    #         continue
    #     ret_val += karakter

    ret_val = tekst.replace(x, y, -1)
    return ret_val

print(zamijeni_karaktere("a", "z"))
