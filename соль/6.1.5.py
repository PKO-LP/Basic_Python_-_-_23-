name = data[0]

quantity = int(data[1][0]) + int(data[1][1])

description = ", ".join(data[2])

prices = [float(data[3][0]), float(data[3][1]), float(data[3][2])]
average_price = round(sum(prices) / 3)

review = data[4]

print(f"Название: {name}")
print(f"Количество: {quantity}")
print(f"Описание товара: {description}")
print(f"Средняя цена: {average_price}")
print(f"Отзыв: {review}")