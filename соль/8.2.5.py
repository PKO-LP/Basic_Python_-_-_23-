# Проходим по предметам и соответствующим оценкам одновременно
for subject, estimate_list in zip(subjects, estimates):
    # Преобразуем список оценок в строку через запятую
    estimates_str = ", ".join(map(str, estimate_list))
    # Выводим предмет и оценки в нужном формате
    print(f"{subject}: {estimates_str}")