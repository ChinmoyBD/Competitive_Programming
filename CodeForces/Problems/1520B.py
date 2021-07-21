for _ in range(int(input())):
    n = int(input())
    if n <= 9:
        print(n)
    elif n <= 100:
        print(9*1 + (n//11))
    elif n <= 1000:
        print(9*2 + (n//111))
    elif n <= 10000:
        print(9*3 + (n//1111))
    elif n <= 100000:
        print(9*4 + (n//11111))
    elif n <= 1000000:
        print(9*5 + (n//111111))
    elif n <= 10000000:
        print(9*6 + (n//1111111))
    elif n <= 100000000:
        print(9*7 + (n//11111111))
    elif n <= 1000000000:
        print(9*8 + (n//111111111))