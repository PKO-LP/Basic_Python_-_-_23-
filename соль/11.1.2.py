# Принимаем строку от пользователя
s = input()

# Создаем функцию для преобразования в вещественное число
def to_float(string):
    try:
        # Пробуем преобразовать строку в float
        return float(string)
    except ValueError:
        # Если не получается, возвращаем None
        return None

# Вызываем функцию и выводим результат
print(to_float(s))