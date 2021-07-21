for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    even = []
    for i in arr:
        if i % 2 != 0:
            print(i, end=' ')
        else:
            even.append(i)
    l = len(even)
    for o in even:
        print(o, end=' ')
    print()