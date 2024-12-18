import turtle as t

def crtanjetacke(x, y, z):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.circle(z)
    t.end_fill()
