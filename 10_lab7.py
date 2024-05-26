"""
Лабораторна робота №7

Задача 1.
Створення завдання з програмування для учнів 7 класу з використанням модуля turtle.

Виконала студетка 31І групи Гриб Наталія
"""


import turtle

# Налаштування екрану
screen = turtle.Screen()
screen.bgcolor("white")

# Налаштування черепашки
t = turtle.Turtle()
t.speed(5)

# Функція для малювання зірки
def draw_star(x, y, size):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.setheading(-72)  # Початковий кут
    for _ in range(5):
        t.forward(size)
        t.right(144)  # Кут повороту для створення зірки
    t.penup()

# Координати та розмір зірок
star_size = 50
star_positions = [
    (-100, 100), (100, 100),  # Верхні лівий і правий
    (-100, -100), (100, -100),  # Нижні лівий і правий
    (-200, 0), (200, 0)  # Лівий центр і правий центр
]

# Малюємо 6 зірок
for pos in star_positions:
    draw_star(pos[0], pos[1], star_size)

# Завершення
t.hideturtle()
turtle.done()