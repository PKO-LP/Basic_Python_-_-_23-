# Принимаем первую строку и преобразуем в кортеж
right_answer = tuple(input().split())
# Принимаем вторую строку и преобразуем в кортеж
person_answer = tuple(input().split())

# Счетчик правильных ответов
correct_count = 0

# Сравниваем ответы по индексам
for i in range(4):
    if right_answer[i] == person_answer[i]:
        correct_count += 1

# Выводим количество правильных ответов
print(correct_count)