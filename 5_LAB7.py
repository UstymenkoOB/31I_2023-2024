import turtle

t = turtle. Turtle()
t.speed(10)

def draw_square():
    for i in range(4):
        t.forward(100)
        t.right(90)
for i in range(6):
    draw_square() 
    t.left(60) 

turtle.done()