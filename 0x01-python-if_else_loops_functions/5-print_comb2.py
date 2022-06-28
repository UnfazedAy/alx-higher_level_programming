#!/usr/bin/python3
for pnum in range(0, 100):
    if pnum != 99:
        print("{:02d}, ".format(pnum), end='')
    else:
        print("{:02d}".format(pnum))
