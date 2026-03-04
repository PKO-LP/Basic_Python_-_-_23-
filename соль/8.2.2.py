# Создаем переменную для суммы
total = 0

# Используем распаковку в цикле для каждого вложенного списка
for first_half, second_half in list_in:
    # Добавляем голы из обоих таймов к общей сумме
    total += first_half + second_half

# Выводим общую сумму
print(total)