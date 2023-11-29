#!/usr/bin/python3
def fizzbuzz():
    for values in range(1, 101):
        if values % 3 == 0 and values % 5 == 0:
            print("FizzBuzz ", end="")
        elif values % 3 == 0:
            print("Fizz ", end="")
        elif values % 5 == 0:
            print("BUZZ ", END="")
        else:
            print("{} ".format(number), end="")
