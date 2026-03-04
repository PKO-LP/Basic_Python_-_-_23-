# Принимаем товары с первого склада и преобразуем в множество
warehouse1 = set(input().split())
# Принимаем товары со второго склада и преобразуем в множество
warehouse2 = set(input().split())

# Объединяем множества (автоматически удаляются дубликаты)
all_products = warehouse1 | warehouse2

# Преобразуем в отсортированный список и выводим
result = sorted(all_products)
print(result)