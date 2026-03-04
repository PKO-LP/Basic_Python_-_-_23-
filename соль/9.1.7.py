# Принимаем строку с именами и преобразуем в список
names_list = input().split()

# Преобразуем список в множество для удаления дубликатов
names_set = set(names_list)

# Создаем множество для имен, которые нужно удалить (начинаются на 'Р')
names_to_remove = set()
for name in names_set:
    if name.startswith('Р'):
        names_to_remove.add(name)

# Удаляем имена на 'Р'
names_set -= names_to_remove

# Добавляем Алона и Эйли
names_set.add('Алон')
names_set.add('Эйли')

# Преобразуем в отсортированный список и выводим
result = sorted(names_set)
print(result)