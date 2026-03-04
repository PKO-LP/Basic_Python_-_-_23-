# Принимаем данные
schedule = input().split()
current = input().split()

# Распаковываем данные
open_time = int(schedule[0])
close_time = int(schedule[1])
day_off = schedule[2]

current_time = int(current[0])
current_day = current[1]

# Проверяем условия
if current_day == day_off:
    print("Закрыто")
elif current_time < open_time or current_time >= close_time:
    print("Закрыто")
else:
    print("Открыто")