for _ in range(int(input())):
    n, k, d = map(int, input().split())
    ps = list(map(int, input().split()))
    contests = sum(ps) // k
    if contests > d:
        print(d)
    else:
        print(contests)
