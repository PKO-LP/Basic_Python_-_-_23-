name = result[0]
subject = result[1]
grades = result[2:]

print(f"Имя: {name}")
print(f"Предмет: {subject}")
print(f"Количество 1: {grades.count(1)}")
print(f"Количество 2: {grades.count(2)}")
print(f"Количество 3: {grades.count(3)}")
print(f"Количество 4: {grades.count(4)}")
print(f"Количество 5: {grades.count(5)}")