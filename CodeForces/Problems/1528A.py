for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    minN = maxN = arr[0]
    minI = maxI = 0

    for i in range(1, n):
        if arr[i] < minN:
            minN = arr[i]
            minI = i
        if arr[i] > maxN:
            maxN = arr[i]
            maxI = i
    if minI > maxI:
        minI, maxI = maxI, minI

    print(min([maxI+1, n - minI, (minI+1) + n - maxI]))