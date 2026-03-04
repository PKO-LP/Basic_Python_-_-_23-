# Фильтруем список, оставляя только тех, у кого rating >= 4.5
filtered_persons = [person for person in persons if person['rating'] >= 4.5]

# Сортируем отфильтрованный список по имени
sorted_persons = sorted(filtered_persons, key=lambda x: x['name'])

# Выводим имена
for person in sorted_persons:
    print(person['name'])