ab = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']

for _ in range(int(input())):
    n = int(input())
    s = input()
    ss = ''
    a = z = 0

    for i in s:
        if i == '0':
            if a == 0 == z:
                z = 8
            else:
                z -= (z-a) // 2
        elif i == '1':
            if a == 0 == z:
                a = 8
                z = 16
            else:
                a += (z-a) // 2
        if z - a == 1:
            ss += ab[a]
            a = z = 0
    print(ss)