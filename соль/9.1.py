# Принимаем строку с предметами и разбиваем на список
subjects = input().split()
# Преобразуем список в кортеж
subjects_tuple = tuple(subjects)
# Выводим кортеж
print(subjects_tuple)