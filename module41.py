import math

# 1. Генерация списка квадратов с использованием list comprehension
# range(1, 11) дает числа от 1 до 10, i**2 - возведение в квадрат
squares = [i ** 2 for i in range(1, 11)]
print("1.", squares)

# 2. Создание словаря дней недели с порядковыми номерами
# enumerate(week_days) возвращает пары (индекс, значение), начиная с 0, поэтому i+1
week_days = ["Понедельник", "Вторник", "Среда", "Четверг", 
             "Пятница", "Суббота", "Воскресенье"]
day_numbers = {day: i+1 for i, day in enumerate(week_days)}
print("2.", day_numbers)

# 3. Создание множества тегов библиотек в нижнем регистре
libraries = ["Django", "FastAPI", "Numpy", "PYTHON", 
             "Pandas", "FASTAPI", "Python", "random"]
tags_lowrr = {lib.lower() for lib in libraries}
print("3.", tags_lowrr)

# 4. Фильтрация четных чисел из списка
# Условие if n % 2 == 0 оставляет только четные числа
numbers_list = [1, 3, 4, 87, 98, 15, 7, 4]
even_numbered = [n for n in numbers_list if n % 2 == 0]
print("4.", even_numbered)

# 5. Создание словаря с факториалами чисел
# math.factorial(i) вычисляет факториал числа i
factorials_dict = {n: math.factorial(n) for n in range(1, 6)}
print("5.", factorials_dict)
