for _ in range(int(input())):
    a, b, c, d = map(int,input().split())

    res = ''
    if a < b:
        a, b = b, a
    if c < d:
        c, d = d, c

    if a > d and c > b:
        print("YES")
    else:
        print("NO")