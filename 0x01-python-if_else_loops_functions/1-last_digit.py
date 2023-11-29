#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ken = abs(number) % 10
if number < 0:
    ken = -ken
print(f"Last digit of {number:d} is {ken:d} and is ", end="")
if ken > 5:
    print("greater than 5")
elif ken == 0:
    print("0")
else:
    print("less than 6 and not 0")
