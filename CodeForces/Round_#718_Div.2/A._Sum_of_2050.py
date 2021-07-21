for _ in range(int(input())):
    n = int(input())
    count = 0
    for i in range(18, -1, -1):
        sn = 2050 * (10 ** i)
        if sn <= n >= 2050:
            tm = n // sn
            n -= sn*tm
            count += tm
        if n < 2050 and n != 0:
            count = -1
            break
    print(count)