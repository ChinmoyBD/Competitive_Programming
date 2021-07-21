from math import gcd
for _ in range(int(input())):
    k = int(input())
    g = gcd(k, 100-k)
    print(k//g + (100-k)//g)