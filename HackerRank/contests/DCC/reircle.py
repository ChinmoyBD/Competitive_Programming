import math
t = int(input())
for i in range(1, t+1):
    pi = math.pi
    radius = float(input())

    print("Case {}: {:.2f}".format(i, 4.0*radius*radius - pi * radius*radius))