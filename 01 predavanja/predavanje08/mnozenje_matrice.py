import os; os.system("cls")

matA = [[1,2],
        [4,5],
        [7,8],
        [4,5]]
matB = [[1,2,3],
        [4,5,6]]
matC = [[0,0,0],
        [0,0,0],
        [0,0,0],
        [0,0,0]]

for i in range(len(matA)):          # petlja po redovima A
    for j in range(len(matB[0])):   # petlja po kolonama B
        for k in range(len(matB)):  # petlja po redovima B
            matC[i][j] = matC[i][j] + matA[i][k] * matB[k][j]
            print("i =", i, "j =", j, "k =", k, "C =", matC[i][j])

print(matC)
