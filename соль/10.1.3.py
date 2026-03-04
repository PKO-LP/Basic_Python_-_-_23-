# Принимаем строку с предметами и разбиваем на список
subjects = input().split()

# Создаем пустой словарь
grades_dict = {}

# Для каждого предмета принимаем строку с оценками
for subject in subjects:
    # Принимаем строку с оценками и преобразуем в список целых чисел
    grades = list(map(int, input().split()))
    # Добавляем предмет и его оценки в словарь
    grades_dict[subject] = grades

# Выводим словарь
print(grades_dict)