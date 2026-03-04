# Принимаем строку и разбиваем на слова
words = input().split()

# Множество для уникальных слов
unique_words = set()
# Множество для слов с дубликатами
duplicate_words = set()

# Проходим по каждому слову
for word in words:
    # Если слово уже встречалось, добавляем его в дубликаты
    if word in unique_words:
        duplicate_words.add(word)
    else:
        unique_words.add(word)

# Выводим количество слов с дубликатами
print(len(duplicate_words))