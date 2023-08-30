#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    total_weight_sum = 0
    weight_total = 0

    for tup in my_list:
        total_weight_sum += tup[0] * tup[1]
        weight_total += tup[1]

    return (total_weight_sum / weight_total)
