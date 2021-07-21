#!/bin/python3

import math
import os
import random
import re
import sys


def birthdayCakeCandles(ar):
    ma = max(ar)
    co = ar.count(ma)
    print(co)


if __name__ == '__main__':
    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    birthdayCakeCandles(ar)
