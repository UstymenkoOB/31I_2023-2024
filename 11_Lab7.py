from turtle import *
import random

speed(10)
pensize(10)
for i in range(6):
    r = random.random()
    g = random.random()
    b = random.random()
    
    color(r,g,b)
    forward(100)
    right(60)

mainloop()
