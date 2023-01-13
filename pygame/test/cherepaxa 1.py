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
def body():
    move(0, 100)

body()

turtle.done()





