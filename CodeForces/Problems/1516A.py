for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    for _ in range(k):
        for i in range(n-1):
            if arr[i] > 0:
                arr[i] -= 1
                arr[-1] += 1
                break
    # print
    print(*arr)