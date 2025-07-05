import turtle

t = turtle.Turtle()
t.pensize(2)
t.speed(3)

for i in range(3):
    t.penup()
    t.goto(0, 3)         
    t.setheading(45)    
    t.right(i * 25)    
    t.pendown()

    for _ in range(4):
        t.forward(100)
        t.right(90)

t.hideturtle()
turtle.done()