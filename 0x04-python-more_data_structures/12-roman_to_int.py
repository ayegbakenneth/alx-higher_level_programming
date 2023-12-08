#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    men = 0
    ten = 0
    face = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for p in reversed(roman_string):
        ten = face[p]
        men += ten if men < ten * 5 else -ten
        return men
