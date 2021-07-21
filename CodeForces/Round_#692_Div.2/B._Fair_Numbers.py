for _ in range(int(input())):
    n = int(input())
    while True:
        s = str(n)
        for i in s:
            if i != '0' and n % int(i) != 0:
                break
        else:
            break
        n += 1
    print(n)
