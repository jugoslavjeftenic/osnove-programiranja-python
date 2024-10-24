import os; os.system("cls")

def prebroj_nule(n):
    brojac = 0
    # str_broj = str(n)
    # for broj in (reversed(str_broj)):
    # for broj in (str_broj[::-1]):
    #     if broj == "0":
    #         brojac += 1
    #     else:
    #         break

    while n % 10 == 0 and n != 0:
        n /= 10
        brojac += 1
    return brojac

print(prebroj_nule(402000))
