from turtle import *
import random

speed(10)
pensize(10)
for i in range(9):
    r = random.random()
    g = random.random()
    b = random.random()
    
    color(r,g,b)
    forward(150)
    right(160)

mainloop()
