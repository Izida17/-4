def append_lines(new_text, file_p):
    """
    Добавляет текст в конец файла и выводит все четные строки файла.
    
    Параметры:
        new_text (str): Текст для добавления в файл
        file_p (str): Путь к файлу
    Использует:
        - Контекстный менеджер для безопасной работы с файлами
        - Режим 'a' для добавления текста
        - Режим 'r' для чтения файла
        - enumerate() для работы с индексами строк
    """
    
    # Добавляем текст в файл с обработкой возможных ошибок
    try:
        with open(file_p, 'a', encoding='utf-8') as file:
            file.write(f"{new_text}\n")  # Добавляем текст с новой строки
    except PermissionError:
        print("Ошибка: Нет прав для записи в файл.")
        return
    except OSError as e:
        print(f"Ошибка при записи в файл: {e}")
        return
    
    # Читаем и выводим четные строки
    try:
        with open(file_p, 'r', encoding='utf-8') as file:
            lines = file.readlines()  # Получаем все строки
            
            print("\nСодержимое четных строк файла:")
            for n, line_content in enumerate(lines, start=1):
                # Нумерация строк начинается с 1, поэтому четные - это n % 2 == 0
                if n % 2 == 0:
                    print(f"{n}: {line_content.strip()}")
                    
    except FileNotFoundError:
        print(f"Файл {file_p} не найден.")
    except UnicodeDecodeError:
        print("Ошибка: Файл содержит некорректные символы.")
    except Exception as e:
        print(f"Неожиданная ошибка при чтении файла: {e}")


# Пример использования
append_lines("Пятая строка", "example.txt")
