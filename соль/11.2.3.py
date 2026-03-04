# Сортируем список persons по двум ключам:
# 1. По отсутствию вредных привычек (False идут первыми)
# 2. По возрасту (чем старше, тем выше)
sorted_persons = sorted(persons,
                        key=lambda x: (x['bad_habits'], -x['age']))

# Выводим результат
for person in sorted_persons:
    print(person)