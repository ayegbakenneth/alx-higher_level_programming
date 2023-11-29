#!/usr/bin/python3
for ken0 in range(0, 10):
    for ken1 in range(ken0 + 1, 10):
        if ken0 == 8 and ken1 == 9:
            print("{}{}".format(ken0, ken1))
        else:
            print("{}{}".format(ken0, ken1), end=", ")
