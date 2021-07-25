for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    s = sum(arr)

    if s == n:
        print(0)
    elif s < n:
        print(1)
    else:
        print(s-n)