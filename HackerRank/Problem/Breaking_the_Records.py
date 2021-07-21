#!/bin/python3

import math
import os
import random
import re
import sys


def breakingRecords(scores):
    maxi = scores[0]
    mini = scores[0]
    hi_score = 0
    lo_score = 0
    for i in scores:
        if i > maxi:
            hi_score += 1
            maxi = i
        elif i < mini:
            lo_score += 1
            mini = i
    print(hi_score, lo_score)


if __name__ == '__main__':
    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)
