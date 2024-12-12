import os; os.system("cls")

def spoj_rjecnike(r1, r2):
    return {i: r1.get(i, 0) + r2.get(i, 0) for i in set(r1).union(r2)}

rjecnik1 = {"kafa": 5, "cokolada": 2}
rjecnik2 = {"voda": 4, "kafa": 3}
print(spoj_rjecnike(rjecnik1, rjecnik2))
