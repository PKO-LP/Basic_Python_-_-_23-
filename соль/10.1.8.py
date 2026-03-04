# Принимаем строку с товарами и разбиваем на список
products = input().split()

# Создаем словарь, где каждому товару соответствует значение 0
stock = {product: 0 for product in products}

# Выводим словарь
print(stock)