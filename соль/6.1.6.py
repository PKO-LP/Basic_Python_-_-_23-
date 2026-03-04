if exchange_rate:
    max_value = max(exchange_rate)
    min_value = min(exchange_rate)
    print(f"Максимальное значение валюты: {max_value}")
    print(f"Минимальное значение валюты: {min_value}")
else:
    print("Максимальное значение валюты: неизвестно")
    print("Минимальное значение валюты: неизвестно")