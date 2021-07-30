for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    countMax = 0
    for i in range(n-1):
        count = arr[i]*arr[i+1]
        if count > countMax:
            countMax = count
    print(countMax)