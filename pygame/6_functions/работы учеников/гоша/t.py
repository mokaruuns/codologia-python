import turtle

t = turtle.Turtle()
#исую квадрат
for i in range(4):
    t.forward(100)
    t.right(90)
#рисую крышу
t.left(45)
t.forward(70)
t.right(90)
t.forward(70)
#рисую трубу
t.left(135)
t.forward(50)
t.left(90)
t.forward(20)
t.left(90)
t.forward(35)
#РИСУЮ ДВЕРЬ
t.penup()
t.forward(115)
t.right(90)
t.forward(10)
t.right(90)
t.pendown()
t.forward(70)
t.left(90)
t.forward(35)
t.left(90)
t.forward(70)
#рисую окно

turtle.done()
