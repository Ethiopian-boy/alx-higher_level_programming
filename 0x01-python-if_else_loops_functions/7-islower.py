#!/usr/bin/python3
def islower(c):
    for i in range(97, 123):
        if (ord(c) >= 97 or ord(c) <= 122):
            return True
        else:
             return False
