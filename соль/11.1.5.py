def super_minus(**kwargs):
    values = list(kwargs.values())
    result = values[0]
    for i in values[1:]:
        result -= i
    return result