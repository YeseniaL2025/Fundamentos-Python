import turtle

t = turtle.Turtle()
t.pensize(2)
t.speed(2)


for _ in range(3):
    t.forward(100)   
    t.left(120)       

t.hideturtle()
turtle.done()