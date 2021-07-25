for _ in range(int(input())):
    n = int(input())
    arr = sorted(list(map(int, input().split())))

    j = 0
    minDis = 10**9
    for i in range(n - 1):
        if arr[i + 1] - arr[i] < minDis:
            minDis = arr[i + 1] - arr[i]
            j = i + 1
    if n == 2:
        print(*arr)
    else:
        print(*arr[j:], *arr[:j])