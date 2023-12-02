#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    ken = len(sys.argv) - 1
    if ken == 0:
        print("0 arguments.")
    elif ken == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(ken))
    for i in range(ken):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
