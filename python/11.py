# Вводим два числа
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))

# Вычисляем модули
abs1 = abs(num1)
abs2 = abs(num2)

# Вычисляем средние значения
average_arithmetic = (abs1 + abs2) / 2
average_geometric = (abs1 * abs2) ** 0.5

# Выводим результаты с округлением
print(f"\nРезультаты:")
print(f"Среднее арифметическое модулей: {average_arithmetic:.2f}")
print(f"Среднее геометрическое модулей: {average_geometric:.2f}")
