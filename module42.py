import math

def is_prime(num):
    """Проверяет, является ли число простым."""
    if num < 2:
        return False
    # Проверяем делители от 2 до квадратного корня числа
    for d in range(2, int(math.sqrt(num)) + 1):
        if num % d == 0:
            return False
    return True

def prime_gener():
    """Генераторная функция для получения простых чисел."""
    ch = 2  
    while True:
        if is_prime(ch):
            yield ch
        ch += 1

# Демонстрация работы генератора
pg = prime_gener()
print("Первые 10 простых чисел:")
for n in range(10):
    print(next(pg))