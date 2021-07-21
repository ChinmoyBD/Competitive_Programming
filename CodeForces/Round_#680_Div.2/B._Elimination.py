for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    a += b
    c += d
    if a > c:
        print(a)
    else:
        print(c)