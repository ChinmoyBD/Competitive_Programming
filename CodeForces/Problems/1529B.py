for _ in range(int(input())):
    n = int(input())
    arr = sorted(list(map(int, input().split())))

    mn = arr[-1]
    count = 1
    for i in range(1, n):
        mn = min(mn, arr[i]-arr[i-1])
        if mn < arr[i]:
            break
        count += 1

    print(count)