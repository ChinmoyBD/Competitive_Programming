'''a, b = map(int, input().split())

n = 1
while True:
    if n == 1:
        if a == 0 or b == 0:
            print(a, b)
            break
        else:
            n = 2

    if n == 2:
        if a >= (2*b):
            a = a % b
            """- (2*b)"""
            n = 1
        else:
            n = 3

    if n == 3:
        if b >= (2*a):
            b = b % a
            """- (2*a)"""
            n = 1
        else:
            print(a, b)
            break
'''

a, b = map(int, input().split())

n = 1
while True:
    if n == 1:
        if a == 0 or b == 0:
            print(a, b)
            break
        else:
            n = 2

    if n == 2:
        if a >= (2*b):
            a = a - (2*b)
            n = 1
        else:
            n = 3

    if n == 3:
        if b >= (2*a):
            b = b - (2*a)
            n = 1
        else:
            print(a, b)
            break
