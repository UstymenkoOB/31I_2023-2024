# Варіант 12
# 
# Напишіть програму, яка реалізує класичний алгоритм бінарного
# пошуку заданого елементу у стовпцях двовимірного масиву. 
# Розмірність масиву та всі елементи генеруються за допомогою випадкових чисел.
# 
# Дзюба Владислав

import random

# Максимальні розміри матриці
MAX_ROWS = 10
MAX_COLS = 10

# Визначаємо розміри матриці випадковим чином
rows = random.randint(1, MAX_ROWS)
cols = random.randint(1, MAX_COLS)

# Генеруємо двовимірний масив із випадкових чисел
matrix = []
for _ in range(rows):
    row = []
    for _ in range(cols):
        row.append(random.randint(1, 100))
    matrix.append(row)

# Виводимо згенеровану матрицю
print("Згенерована матриця:".format(rows, cols))
for row in matrix:
    print(row)

# Заданий елемент для пошуку
target = int(input("Введіть елемент для пошуку: "))

# Шукаємо заданий елемент у стовпцях матриці
for col in range(cols):
    # Отримуємо стовпець як список
    column = [matrix[row][col] for row in range(rows)]
    # Сортуємо стовпець перед бінарним пошуком
    column.sort()
    
    # Бінарний пошук у стовпці
    left, right = 0, len(column) - 1
    found = False
    while left <= right:
        mid = (left + right) // 2
        if column[mid] == target:
            found = True
            break
        elif column[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    if found:
        print(f"Знайдено елемент {target} у стовпці {col + 1}")
    else:
        print(f"Елемент {target} не знайдено у стовпці {col + 1}")
