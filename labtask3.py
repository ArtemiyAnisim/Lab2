# Задача №3 найти наибольшее значение 

def lim_max(nums, limit):
    a = -1
    for i in nums:
        if i < limit and i > a: # условие ограниченного максимума
            a = i
    return a
