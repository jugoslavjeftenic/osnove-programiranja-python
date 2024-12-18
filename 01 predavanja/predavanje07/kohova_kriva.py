import os; os.system("cls")
import turtle

def koh(duzina, dubina):
    if dubina > 0:
        for ugao in (60, -120, 60, 0):
            print("da", duzina, ugao, dubina)
            koh(duzina/3, dubina-1)
            turtle.left(ugao)
            print(ugao)
    else:
        turtle.forward(duzina)
        print("ne")

for i in range(3):
    turtle.right(120)
    koh(400, 2)

turtle.done()
