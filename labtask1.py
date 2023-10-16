# Задача №1 списки имён и фамилий

def list_reorder(ref_list):
    names = ref_list[0] # список имен
    surnames = ref_list[1] # список фамилий
    new = []

    for i in names:
        a = []
        a.append(i) # имя из первого списка
        a.append(surnames[names.index(i)]) # соответсвующая ему по индексу фамилия из второго списка
        new.append(a)

    return new
