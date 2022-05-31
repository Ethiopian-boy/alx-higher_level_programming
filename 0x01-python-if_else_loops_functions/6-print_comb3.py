#!/usr/bin/python3
for i in range(10):
    if (i != 8):
        for j in range(i+1, 10):
            print(f"{i}{j}", end=', ')
    else:
        print(f"{i}{i+1}")
