import turtle

alex=turtle.Turtle()

w=turtle.Screen()
w.bgcolor("violet")

def desenharQuadrado(t, tam):
    for i in range(4):
        t.forward(tam)
        t.left(90)


desenharQuadrado(alex, 20)

