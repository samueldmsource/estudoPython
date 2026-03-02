import turtle

wn = turtle.Screen()

alexy = turtle.Turtle()

for i in [0,1,2,3,4]:
    alexy.forward(150)
    alexy.left(90)
    alexy.forward(75)
    alexy.left(90)
    alexy.forward(150)
    alexy.left(90)
    alexy.forward(75)

wn.exitonclick()