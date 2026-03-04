# Проходим по каждому товару в словаре stock
for product, quantity in stock.items():
    # Проверяем количество товара
    if quantity > 0:
        # Если товар есть в наличии
        print(f"Товар: {product}, остаток: {quantity} шт")
    else:
        # Если товара нет
        print(f"Товар: {product}, отсутствует")