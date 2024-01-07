#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0:
        if len(tuple_b) == 0:
            sum_0 = 0
        else:
            sum_0 = tuple_b[0]
    else:
        if len(tuple_b) == 0:
            sum_0 = tuple_a[0]
        else:
            sum_0 = tuple_a[0] + tuple_b[0]
    if len(tuple_a) == 1:
        if len(tuple_b) <= 1:
            sum_1 = 0
        else:
            sum_1 = tuple_b[1]
    else:
        if len(tuple_b) <= 1:
            sum_1 = tuple_a[1]
        else:
            sum_1 = tuple_a[1] + tuple_b[1]
    return (sum_0, sum_1)
