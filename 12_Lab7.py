from turtle import *
import random

turtle = Turtle()
speed(10)
color("blue")

for i in range(9):
    r = random.random()
    g = random.random()
    b = random.random()
    
    color(r,g,b)
    forward(150)
    right(160)

mainloop()
