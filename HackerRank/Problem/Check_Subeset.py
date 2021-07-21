for _ in range(int(input())):
    a = int(input())
    arr = list(map(int, input().split()))

    b = int(input())
    brr = list(map(int, input().split()))

    arr = set(arr)

    brr = set(brr)

    c = arr & brr

    if len(arr) == len(c):
        print(True)
    else:
        print(False)

