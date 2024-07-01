import turtle as TL


window = TL.Screen()
window.title("Figuras Geométricas")
window.bgcolor("white")


t = TL.Turtle()
t.speed(1)  


def Dibujo_Cuadrado(t, lado):
    for _ in range(4):
        t.forward(lado)
        t.right(90)

def Dibujar_Rectangulo(t, ancho, altura):
    for _ in range(2):
        t.forward(ancho)  
        t.right(90)
        t.forward(altura)
        t.right(90)


t.penup()
t.goto(-150, 0)
t.pendown()
Dibujo_Cuadrado(t, 100)


t.penup()
t.goto(50, 0)
t.pendown()
Dibujar_Rectangulo(t, 150, 100)


window.mainloop()


