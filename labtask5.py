# Задача №5 возрат списков

def check_phn(phones):
    for i in phones:
        if i[0] == '+':
            count = 1
            if i[1] == '7' or i[1] == '8':
                for x in i[2:]:
                    if x == ' ' or x == '-' or x == '(' or x == ')':
                        continue
                    elif x in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'):
                        count += 1
                    else:
                        return -1
                if count != 11:
                    return -1
