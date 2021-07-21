#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    ma = max(arr)
    mi = min(arr)
    a = sum(arr) - ma
    b = sum(arr) - mi
    print(a, b)
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
