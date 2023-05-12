#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    import calculator_1 as cal

    args = sys.argv
    argc = len(args) - 1

    if argc != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    if args[2] == "+":
        print(
            "{} {} {} = {}".format(
                args[1], args[2], args[3], cal.add(int(args[1]), int(args[3]))
            )
        )
    elif args[2] == "-":
        print(
            "{} {} {} = {}".format(
                args[1], args[2], args[3], cal.sub(int(args[1]), int(args[3]))
            )
        )
    elif args[2] == "*":
        print(
            "{} {} {} = {}".format(
                args[1], args[2], args[3], cal.mul(int(args[1]), int(args[3]))
            )
        )
    elif args[2] == "/":
        print(
            "{} {} {} = {}".format(
                args[1], args[2], args[3], cal.div(int(args[1]), int(args[3]))
            )
        )
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
