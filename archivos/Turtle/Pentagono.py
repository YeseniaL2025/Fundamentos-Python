import turtle

t = turtle.Turtle()
t.pensize(2)
t.speed(2)


for _ in range(5):
    t.forward(80)   
    t.left(72)       

t.hideturtle()
turtle.done()