import os; os.system("cls")

# Napisati funkciju prebroj_cifre koja kao parametar prima prirodan broj n,
# a vraća broj pojavljivanja cifre 5 u tom broju.
# Na primer, poziv prebroj_cifre(152555) treba da vrati 3.

def prebroj_cifre(n):
    ret_val = 0
    while n > 0:
        if n % 10 == 5:
            ret_val += 1
        n //= 10

    return ret_val
    # return str(n).count("5")

print(prebroj_cifre(1525555))
