def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)


li = [12, 42, 54]
a = li[0]
for i in range(1, 3):
    b = li[i]
    a = gcd(a, b)
print(a)