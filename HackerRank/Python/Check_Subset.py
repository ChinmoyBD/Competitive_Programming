for _ in range(int(input())):
    a = int(input())
    arr = set(map(int, input().split()))
    
    b = int(input())
    brr = set(map(int, input().split()))

    if brr == brr | arr:
        print(True)

    else:
        print(False)