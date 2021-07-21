for _ in range(int(input())):
    # n, x, t = map(int, input().split())
    #
    # if x > t:
    #     print(0)
    # elif x == t:
    #     print(n-1)
    # else:
    #     a = t//x
    #     if a >= n:
    #         print((n(n-1))//2)
    #     else:
    #

    st = input().strip()
    std = '['
    le_n = len(st)
    for i in range(le_n):
        if le_n - 1 == i:
            std += '"' + st[i] + '"'
        else:
            std += '"' + st[i] + '"' + ', '
    std += ']'
    print(std)
