#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sute = 0
    for j in range(len(sys.argv) - 1):
        sute += int(sys.argv[j + 1])
    print(sute)
