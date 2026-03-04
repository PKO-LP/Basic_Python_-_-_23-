# Принимаем число от пользователя
n = int(input())

# Создаем функцию для проверки четности
def check_even_odd(number):
    if number % 2 == 0:
        print("Число чётное")
    else:
        print("Число нечётное")

# Вызываем функцию с переданным числом
check_even_odd(n)