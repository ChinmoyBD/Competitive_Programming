for _ in range(int(input())):
    n = int(input())
    count = 0
    for i in range(1, 200, 2):
        count += 1
        n -= i
        if n <= 0:
            break
    print(count)