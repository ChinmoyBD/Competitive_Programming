import math
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    count = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if math.gcd(arr[i], (arr[j])*2) > 1 or math.gcd((arr[i])*2, arr[j]) > 1:
                count += 1
    print(count)