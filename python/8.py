def user_info():
    # Запрашиваем информацию у пользователя
    name = input("Как тебя зовут? ")
    age = input("Сколько тебе лет? ")
    city = input("Где ты живешь? ")
    
    # Выводим информацию
    print(f"Это {name}")
    print(f"Ему {age} лет")
    print(f"Он живет в {city}")

# Вызываем функцию
if __name__ == "__main__":
    user_info()
