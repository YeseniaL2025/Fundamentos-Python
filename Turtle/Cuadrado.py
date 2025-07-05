import turtle

t = turtle.Turtle()
t.pensize(2)
t.speed(2)


for _ in range(4):
    t.forward(150)   
    t.left(90)       

t.hideturtle()
turtle.done()