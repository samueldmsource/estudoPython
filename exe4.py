import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()

tess.shape("turtle")
tess.penup()
tess.color("violet")
tess.stamp()
tess.speed(0)

raio = 150

for i in range(12):
    tess.goto(0,0)
    tess.setheading(i * 30) #360/12=30
    tess.forward(raio)
    tess.stamp()

centro = turtle.Turtle()
centro.color("lightgreen")
centro.speed(0)
centro.goto(0,0)
centro.hideturtle()
centro.penup()
centro.stamp()



wn.exitonclick()

#for size in range(1,13,8):      # começar com size = 5 e passo 2
    #tess.color("violet")
    #tess.stamp()                # deixar um carimbo no canvas          # tess, vá para frente
    #tess.speed(0)
#wn.exitonclick()