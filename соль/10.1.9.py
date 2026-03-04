# Принимаем оценки для Анны, Бориса и Виктории
anna_grades = list(map(int, input().split()))
boris_grades = list(map(int, input().split()))
victoria_grades = list(map(int, input().split()))

# Добавляем оценки Анне
students["Анна"]["математика"].append(anna_grades[0])
students["Анна"]["физика"].append(anna_grades[1])
students["Анна"]["химия"].append(anna_grades[2])

# Добавляем оценки Борису
students["Борис"]["математика"].append(boris_grades[0])
students["Борис"]["физика"].append(boris_grades[1])
students["Борис"]["химия"].append(boris_grades[2])

# Добавляем оценки Виктории
students["Виктория"]["математика"].append(victoria_grades[0])
students["Виктория"]["физика"].append(victoria_grades[1])
students["Виктория"]["химия"].append(victoria_grades[2])

# Выводим обновленный словарь
print(students)