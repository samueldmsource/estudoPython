import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.shape("turtle")
tess.color("violet")
tess.penup()
tess.speed(0)

# Raio do relógio
raio = 150

# Desenha as 12 tartarugas na borda
for i in range(12):
    tess.goto(0, 0)
    tess.setheading(i * 30)  # gira 30 graus
    tess.forward(raio)
    tess.stamp()

# Tartaruga do centro
centro = turtle.Turtle()
centro.shape("turtle")
centro.color("green")
centro.penup()
centro.goto(0, 0)
centro.stamp()
centro.hideturtle()

wn.exitonclick()
