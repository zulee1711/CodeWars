import numpy as np

def filter_list(l):
    list = []
    for i in l:
        if type(i) == float:
            continue
        else:
            list.append(i)
    return list


print(filter_list([1,2,'a','b']))