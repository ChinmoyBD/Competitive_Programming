for _ in range(int(input())):
    a, b = map(int,input().split())

    ab = a*2

    s = b - ab
    if s < 0:
        print(-1)
    else:
        print(s)