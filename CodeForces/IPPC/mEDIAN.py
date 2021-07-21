import math
n = int(input())
arr = sorted(list(map(int, input().split())))

a = math.floor(n/2)
b = math.ceil(n/2)

result = int((arr[a] + arr[b]) / 2)
print(result)