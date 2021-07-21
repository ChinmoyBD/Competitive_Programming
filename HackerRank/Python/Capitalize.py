import math
import os
import random
import re
import sys


def solve(s):
    s_t = s.strip()
    for i in s_t[:].split():
        s_t = s_t.replace(i, i.capitalize())
    print(s_t)

if __name__ == '__main__':

    s = input()

    solve(s)