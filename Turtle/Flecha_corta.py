import turtle

t = turtle.Turtle()
t.pensize(2)
t.speed(1)

for _ in range(10):
    t.pendown()
    t.forward(10)
    t.penup()
    t.forward(5)


t.pendown()
t.right(150)
t.forward(20)
t.backward(20)
t.left(300)
t.forward(20)
t.backward(20)
t.right(150)


t.hideturtle()
turtle.done()