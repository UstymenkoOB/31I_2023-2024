"""
Задача №1.
Намалювати фігуру, яка складається з 6 трикутників з використанням модуля turtle.

Автор: Волочнюк Поліна
"""
from turtle import *

# Створення об'єкту 
t = Turtle()
t.shape("turtle")
# Налаштування швидкості 
t.speed(3)

# Малювання фігури
for i in range(6):
    for i in range(3):
        t.forward(100)
        t.right(120)
    t.right(60)


