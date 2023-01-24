import turtle

t = turtle.Turtle()
t.speed(0)


def wheel():
    for i in range(360):
        t.forward(0.5)
        t.right(1)


def bottom():
    t.forward(100)


def move(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    wheel()
    bottom()
    wheel()
    boby()
    cabin()
    glass()


def boby():
    t.forward(10)
    t.left(90)
    t.forward(70)
    t.left(90)
    t.forward(85)
    t.left(90)
    t.forward(70)
    t.left(180)


def cabin():
    t.forward(60)
    t.left(90)
    t.forward(25)
    for i in range(90):
        t.forward(0.1)
        t.left(1)
    t.forward(20)
    t.right(90)
    t.forward(10)
    t.left(90)
    t.forward(40)


def glass():
    t.penup()
    t.left(180)
    t.forward(40)
    t.right(90)
    t.forward(10)
    t.pendown()
    t.forward(10)
    t.left(90)
    t.forward(10)
    for i in range(180):
        t.left(1)
        t.forward(0.1)


move(0, 100)

turtle.done()
