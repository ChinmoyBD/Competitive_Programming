for _ in range(int(input())):
    n = int(input())
    count = 2

    while count <= n:
        count *= 2
    print((count//2)-1)