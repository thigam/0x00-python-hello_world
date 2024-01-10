#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or not my_list:
        return 0
    sum = 0
    denom = 0
    for i, j in my_list:
        sum += (i * j)
        denom += j
    return sum / denom
    
