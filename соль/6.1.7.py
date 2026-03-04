grades = list(map(int, input().split()))
average = sum(grades) / len(grades)
print(f"Оценка за четверть: {round(average)}")