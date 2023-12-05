#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    ken = my_list[:]
    if 0 <= idx < len(my_list):
        ken[idx] = element
        return(ken)
    return(ken)
