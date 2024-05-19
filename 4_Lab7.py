# Імпорт графічного модуля turtle
import turtle

# Створення нового об'єкту turtle
t = turtle.Turtle()
# Створення нового об'єкту екрану
s = turtle.Screen()

# Встановлення фонового кольору екрана на чорний
s.bgcolor("black")
# Встановлення кольору малювання turtle на блакитний
t.pencolor("cyan")
# Встановлення швидкості черепахи на максимальну
t.speed(0)
# Черепаха піднімає ручку, щоб не малювати, коли рухається
t.penup()
# Переміщення черепашки у координати (0, 260) без малювання
t.goto(0, 260)
# Опускає ручку, щоб почати малювати
t.pendown()


# Початкові значення координат
x = 0
y = 0

# Запуск циклу
while y < 310:
    # Переміщення черепашки вперед на 'x' одиниць
    t.forward(x)
    # Обертання черепашки вправо на 'y' градусів
    t.right(y)
    # Збільшення 'x' на 3
    x += 3
    # Збільшення 'y' на 1
    y += 1

# Закриття програми при закритті вікна
turtle.done()
