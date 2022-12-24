import turtle

t = turtle.Turtle()
t.pencolor("green")
t.begin_fill()

for i in range(360):
    t.pendown()
    t.forward(1)
    t.right(1)
for i in range(3):
    t.forward(100)
    t.right(120)
t.end_fill()
t.penup()
t.forward(200)
t.pendown()

t.fd(100)
turtle.done()
t.right(90)

for i in range(360):
    t.pendown(1)
    t.right(1)
