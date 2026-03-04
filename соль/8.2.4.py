# Принимаем строку с оценками и преобразуем в список чисел
grades = list(map(int, input().split()))

# Находим самую высокую оценку (без использования max)
highest_grade = grades[0]  # предполагаем, что первый элемент - самый высокий
for grade in grades:
    if grade > highest_grade:
        highest_grade = grade

# Считаем количество самой высокой оценки (без использования .count())
count = 0
for grade in grades:
    if grade == highest_grade:
        count += 1

# Выводим результат
print(f"Самая высокая оценка: {highest_grade}")
print(f"Количество: {count} шт")