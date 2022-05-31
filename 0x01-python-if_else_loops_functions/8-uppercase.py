#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        n = ord(str[i])
        if(n >= 97 and n <= 122):
            n -= 32
        print("{}".format(chr(n)), end='')
    print()
