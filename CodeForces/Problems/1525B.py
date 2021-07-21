for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    count = 0
    for i in range(n):
        if arr[i] != i+1:
            count += 1
    if count == 0:
        print(0)
    elif arr[0] == 1 or arr[-1] == n:
        print(1)
    elif arr[0] == n and arr[-1] == 1:
        print(3)
    else:
        print(2)