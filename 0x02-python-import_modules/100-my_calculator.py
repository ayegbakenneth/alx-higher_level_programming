#!usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    c = int(sys.argv[1])
    d = int(sys.argv[3])
    ken = sys.argv[2]
    if ken == "+":
        print("{} + {} = [}".format(c, d, add(c, d)))
    elif ken == "-":
        print("{} - {} = {}".format(c, d, sub(c, d)))
    elif ken == "*":
        print("{} * {} = {}".format(c, d, sub(c, d)))
    elif ken == "/":
        print("{} / {} = {}".format(c, d, div(c, d)))
    else:
        print("Unknown operator, Available operators: +, -, * and /")
        exit(1)

