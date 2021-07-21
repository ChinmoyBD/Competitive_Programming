for _ in range(int(input())):
    x = int(input())
    if x % 2 == 0:
        a = b = x // 2
        if (a & b) + (a | b) == x:
            print(a, b)
        else:
            print(-1)
    else:
        a = x//2
        b = a+1
        if (a & b) + (a | b) == x:
            print(a, b)
        else:
            print(-1)