def calculate_numbers():
    # Запрашиваем четыре числа у пользователя
    try:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        num3 = float(input("Введите третье число: "))
        num4 = float(input("Введите четвертое число: "))
    except ValueError:
        print("Пожалуйста, введите корректные числа!")
        return
    
    # Складываем первые два и вторые два числа
    sum_first_two = num1 + num2
    sum_second_two = num3 + num4
    
    # Проверяем деление на ноль
    if sum_second_two == 0:
        print("Ошибка: Деление на ноль! Сумма вторых двух чисел равна нулю.")
        return
    
    # Делим первую сумму на вторую
    result = sum_first_two / sum_second_two
    
    # Выводим результат с двумя цифрами после запятой
    print(f"Результат: {result:.2f}")

# Вызываем функцию
if __name__ == "__main__":
    calculate_numbers()
