#!/usr/bin/python3
def uniq_add(my_list=[]):
    deja_vu = []
    total = 0
    for i in my_list:
        if i not in deja_vu:
            total += i
            deja_vu.append(i)
    return total
