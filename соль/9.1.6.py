# Принимаем первую строку с чеками и преобразуем в множество
all_checks = set(map(int, input().split()))

# Принимаем вторую строку с числом клиента
client_number = int(input())

# Проверяем, есть ли число клиента в множестве чеков
if client_number in all_checks:
    print("Осуществляем возврат")
else:
    print("Такой суммы нет")