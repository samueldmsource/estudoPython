import turtle            # cria alex
wn = turtle.Screen()
alex = turtle.Turtle()
alexy = turtle.Turtle()

for i in range (1):  # repita 4 vezes
    alexy.forward(150)
    alexy.left(90)
    alexy.forward(75)
    alexy.left(90)
    alexy.forward(150)
    alexy.left(90)
    alexy.forward(75)

    alex.forward(380)
    alex.left(90)
    alex.forward(200)
    alex.left(90)

    alex.forward(610)
    alex.left(90)
    alex.forward(200)
    alex.left(90)
    alex.forward(230)



wn.exitonclick()

