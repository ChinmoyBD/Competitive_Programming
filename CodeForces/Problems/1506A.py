for _ in range(int(input())):
    n, m, x = map(int, input().split())

    if x % n == 0:
        col = x//n
        row = n
    else:
        col = (x//n) + 1
        row = x % n
    print(m*(row-1)+col)
