def filter_by_age(persons_dict):
    """
    Фильтрует словарь с людьми по возрасту (от 18 до 30 лет включительно)
    и возвращает отсортированный список имён.

    :param persons_dict: словарь с именами и возрастами
    :return: отсортированный список имён
    """
    result = []
    for name, age in persons_dict.items():
        if 18 <= age <= 30:
            result.append(name)
    result.sort()
    return result


# Вызываем функцию и выводим результат
filtered_names = filter_by_age(persons)
print(filtered_names)