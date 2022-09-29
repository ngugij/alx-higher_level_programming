#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list and len(my_list):
        score = 0
        weight = 0
        for pair in my_list:
            score = score + (pair[0] * pair[1])
            weight = weight + pair[1]
        return (score / weight)
    return (0)
