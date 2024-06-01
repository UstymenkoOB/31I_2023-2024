# Варіант 12
# 
# Дано число. Знайти мінімальну кількість степенів двійки, що у сумі дорівнюють цьому числу.
# 
# Дзюба Владислав

def min_powers_of_two(n):
    powers = []
    while n > 0:
        power = 1
        while power <= n:
            power <<= 1
        power >>= 1
        powers.append(power)
        n -= power
    return powers

number = int(input("Введіть число: "))
result = min_powers_of_two(number)
print(f"Мінімальна кількість степенів двійки, що у сумі дорівнюють {number}: {len(result)}")

