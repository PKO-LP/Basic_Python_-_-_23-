# Принимаем товары на первом складе и преобразуем в множество
warehouse1 = set(input().split())
# Принимаем товары на втором складе и преобразуем в множество
warehouse2 = set(input().split())
# Принимаем обязательный список товаров и преобразуем в множество
required = set(input().split())

# Находим недостающие товары на первом складе
missing1 = sorted(required - warehouse1)
# Находим недостающие товары на втором складе
missing2 = sorted(required - warehouse2)

# Выводим результат
print(f"Склад 1: {missing1}")
print(f"Склад 2: {missing2}")