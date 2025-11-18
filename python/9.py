def arithmetic_test():
    # Правильный ответ
    correct_answer = 4 * 100 - 54
    
    # Запрашиваем ответ у пользователя
    user_answer = input("Решите пример: 4 * 100 - 54 = ")
    
    # Преобразуем ввод пользователя в число
    try:
        user_answer = int(user_answer)
    except ValueError:
        print("Пожалуйста, введите корректное число!")
        return
    
    # Выводим результаты
    print(f"Правильный ответ: {correct_answer}")
    print(f"Твой ответ: {user_answer}")

# Вызываем функцию
if __name__ == "__main__":
    arithmetic_test()
