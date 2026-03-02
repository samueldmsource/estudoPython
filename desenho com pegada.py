import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.color("blue")
tess.shape("triangle")

#print(range(5,60,15))
tess.penup()                    # isso é novo
for size in range(5,60,1):      # começar com size = 5 e passo 2
    tess.color("violet")
    tess.stamp()                # deixar um carimbo no canvas
    tess.forward(size)          # tess, vá para frente
    tess.right(30)              # tess, vire 24 graus a direita

wn.exitonclick()
