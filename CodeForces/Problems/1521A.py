for _ in range(int(input())):
    a, b = map(int, input().split())

    if b == 1:
        print("NO")
    else:
        print("YES")
        good = (a*b)*2
        print(a, good-a, good)