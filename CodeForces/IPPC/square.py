import math
PI = math.pi * 4

a = math.sin((108*PI)/180) / math.sin((63*PI)/180)

n = float(input())
print("{:.10f}".format(a*n))