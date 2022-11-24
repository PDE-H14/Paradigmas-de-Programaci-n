#
# Gráficos usando la tortuga que pinta al caminar
#

import turtle
tortuga = turtle.Turtle()
tortuga.left(90)
tortuga.speed(500)

#
# Con ángulos de 90 es un árbol H
#

angulo: float = 90

#
# El árbol se construye con recursividad 
#

def arbol(i:float, angulo:float):
    if i<10:
        return
    else:
        tortuga.forward(i)
        tortuga.left(angulo)
        arbol(3*i/4.25,angulo)
        tortuga.right(2*angulo)
        arbol(3*i/4.25,angulo)
        tortuga.left(angulo)
        tortuga.backward(i)

arbol(100,angulo)
turtle.done()
