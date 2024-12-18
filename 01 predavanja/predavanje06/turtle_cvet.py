import os; os.system("cls")
import turtle as t

t.color("red")
t.pensize(4)
t.speed(20)
t.pendown()
for i in range(36):
    t.forward(200)
    t.right(170)
    print(t.position())

t.done()
