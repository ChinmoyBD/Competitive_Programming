#!/bin/python3

import math
import os
import random
import re
import sys


def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple_li = []
    for i in apples:
        apple_li.append(a + i)

    orange_li = []
    for i in oranges:
        orange_li.append(b + i)

    apple_count = 0
    for i in apple_li:

        if (i >= s) and (i <= t):
            apple_count += 1
    print(apple_count)

    orange_count = 0
    for i in orange_li:

        if (i >= s) and (i <= t):
            orange_count += 1
    print(orange_count)


if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
