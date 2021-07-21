while True:
    a, b, c = map(int, input().split())

    if a == b == c == 0:
        break

    if a > c:
        a, c = c, a
    if b > c:
        b, c = c, b

    if a*a + b*b == c*c:
        print("right")
    else:
        print("wrong")