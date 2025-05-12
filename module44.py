def log_function_call(function):
    """
    Декоратор для логирования вызовов функций.
    Выводит информацию о функции, её аргументах и результате выполнения.
    """
    def enhanced_function(*args, **kwargs):
        # Выводим информацию о вызове функции
        print(f"\n Функция {function.__name__} вызвана с аргументами:")
        print(f"Позиционные аргументы: {args}")
        print(f"Именованные аргументы: {kwargs}")
        
        # Выполняем оригинальную функцию
        calculation = function(*args, **kwargs)
        
        # Возвращаем результат для возможности его использования
        return calculation
    
    return enhanced_function

@log_function_call
def calculate_rect_area(a, b):
    """
    Вычисляет площадь прямоугольника.
    
    Аргументы:
        a (int/float): длина одной стороны
        b (int/float): длина другой стороны
        
    Возвращает:
        int/float: площадь прямоугольника
    """
    area = a * b
    print(f"Площадь прямоугольника: {area}")
    return area

# Демонстрация работы
calculate_rect_area(6, 8)  # Позиционные аргументы
calculate_rect_area(a = 2, b = 6)  # Именованные аргументы
calculate_rect_area(4, b = 9)  # Смешанные аргументы
