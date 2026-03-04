# Принимаем 4 строки и преобразуем в множества
you_info = set(input().split())
your_requirements = set(input().split())
partner_info = set(input().split())
partner_requirements = set(input().split())

# Считаем совпадения между вашей информацией и требованиями партнера
match1 = len(you_info & partner_requirements)
# Считаем совпадения между вашими требованиями и информацией партнера
match2 = len(your_requirements & partner_info)

# Складываем совпадения для получения рейтинга
rating = match1 + match2

# Выводим рейтинг
print(rating)