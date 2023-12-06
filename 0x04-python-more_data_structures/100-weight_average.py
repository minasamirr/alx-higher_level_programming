#!/usr/bin/python3
def weight_average(my_list=[]):
    weighted_sum, total_weight = map(sum, zip(*[(score * weight, weight) for score, weight in my_list]))
    if total_weight == 0:
        return 0
    return (weighted_sum / total_weight)
