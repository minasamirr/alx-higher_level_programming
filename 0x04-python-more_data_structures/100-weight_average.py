#!/usr/bin/python3
def weight_average(my_list=[]):
    # Calculate the weighted sum and sum of weights using zip and map
    weighted_sum, total_weight = map(sum, zip(*[(score * weight, weight) for score, weight in my_list]))

    # Avoid division by zero
    if total_weight == 0:
        return 0

    # Calculate and return the weighted average
    return weighted_sum / total_weight
