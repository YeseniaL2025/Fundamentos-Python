import turtle

t = turtle.Turtle()
t.pensize(2)
t.speed(2)

ancho = 140
alto = 80

for _ in range(2):
    t.forward(ancho)   
    t.left(90)
    t.forward(alto)    
    t.left(90)

t.hideturtle()
turtle.done()
