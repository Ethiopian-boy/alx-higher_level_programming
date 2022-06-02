#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = len(sys.argv) - 1
    if (n == 0):
        print("{:d} arguments.".format(n))
    elif (n == 1):
        print("{:d} argument:".format(n))
    else:
        print("{:d} arguments:".format(n))
    for str in range(len(sys.argv)):
        if (str == 0):
            continue
        print("{:d}: {:s}".format(str, sys.argv[str]))
