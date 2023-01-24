import turtle as t


def dom(x, y, r):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.goto(x, y + r)
    t.goto(x + r, y + r)
    t.goto(x + r, y)
    t.goto(x, y)
    t.goto(x, y + r)
    t.goto(x - r / 2, y + r)
    t.goto(x + r + r / 2, y + r)
    t.goto(x + r - r / 2, y + r + 100)
    t.goto(x - r / 2, y + r)


dom(- 50, - 50, 150)