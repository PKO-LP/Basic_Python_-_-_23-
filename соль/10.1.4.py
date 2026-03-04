# Принимаем строку и разбиваем на слова
words = input().split()

# Создаем пустой словарь для подсчета слов
word_count = {}

# Подсчитываем количество каждого слова
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Сортируем словарь по ключам
sorted_word_count = dict(sorted(word_count.items()))

# Выводим результат
print(sorted_word_count)