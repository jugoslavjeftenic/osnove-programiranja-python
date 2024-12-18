import turtle as t

def crtanjepravougaonika(x = 0, y = 0, width = 100, height = 200):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.right(90)
    t.forward(height)
    t.right(90)
    t.forward(width)
    t.right(90)
    t.forward(height)
    t.right(90)
    t.forward(width)
