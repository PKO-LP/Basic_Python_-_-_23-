# Принимаем строку с предметами и разбиваем на список
subjects = input().split()

# Создаем пустой словарь
grades_dict = {}

# Добавляем каждый предмет как ключ с пустым списком в качестве значения
for subject in subjects:
    grades_dict[subject] = []

# Выводим словарь
print(grades_dict)