import os; os.system("cls")

def chocolate_eating_competition(n, x, y):
    chocolate_eaters = [0 for _ in range(n)]
    current_chocolate_eater = 0

    while True:
        if x > y:
            x -= y
        else:
            y -= x
        chocolate_eaters[current_chocolate_eater] += 1

        if current_chocolate_eater >= len(chocolate_eaters) - 1:
            current_chocolate_eater = 0
        else:
            current_chocolate_eater += 1

        if x == 0 or y == 0:
            break
    
    return chocolate_eaters

def winner(chocolate_eaters):
    acu_max = 0
    acu_index = 0

    for i in range(len(chocolate_eaters)):
        print("Osoba", i + 1, "je pojela", chocolate_eaters[i], "komadica cokolade.")
        if chocolate_eaters[i] > acu_max:
            acu_max = chocolate_eaters[i]
            acu_index = i
    print()

    # TODO Nije zavrseno. Treba vratiti odgovarajuci rezultat ako su svi pojeli jednak broj cokolade
    return acu_index + 1

result = chocolate_eating_competition(3, 17, 3)
print("Najvise cokolade je pojela osoba", winner(result))
print()
