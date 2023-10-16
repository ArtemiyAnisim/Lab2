# Задача №4 температура

def temp_cat(temp):
    # для каждого случая выводим категорию
    if temp < -20:
        return 0
    if temp <= 0:
        return 1
    if temp <= 15:
        return 2
    if temp <= 25:
        return 3
    else:
        return 4
