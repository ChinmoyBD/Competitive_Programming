for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    maxValue = 0
    for i in range(n):
        tp = arr[i]
        tpi = i + tp
        while tpi < n:
            tp += arr[tpi]
            tpi += arr[tpi]
        if tp > maxValue:
            maxValue = tp
    print(maxValue)