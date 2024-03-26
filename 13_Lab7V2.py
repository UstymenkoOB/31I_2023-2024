import turtle
import random

n = 5

pen = turtle.Turtle()

pen.width(2)

for i in range(n * 3):
    r = random.random()
    g = random.random()
    b = random.random()

    pen.color(r, g, b)

    pen.forward(i * 10)

    pen.right(120)

turtle.done()
