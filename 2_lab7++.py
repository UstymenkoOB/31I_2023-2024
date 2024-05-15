#Задача №1
#Намалюйте світлофор, три кола червоне, жовте та зелене в стовпчик з використанням модуля turtle
#Автор: Бернацька Юлія 31І група
from turtle import *

# Встановлюємо розмір пера
pensize(20)


# Червоне
color('black', 'red')
begin_fill()
up()
goto(0, -120)
down()
circle(60)
end_fill()

# Жовте
color('black', 'yellow')
begin_fill()
up()
goto(0, 0)
down()
circle(60)
end_fill()

# Зелене
color('black', 'green')
begin_fill()
up()
goto(0, 120)
down()
circle(60)
end_fill()


hideturtle()


mainloop()
