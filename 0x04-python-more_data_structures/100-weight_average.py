#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    else:
        return (sum(c * d for c, d in my_list) / sum(d for c, d in my_list))
