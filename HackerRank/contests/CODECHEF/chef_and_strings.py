try:
    t = int(input())

    for _ in range(t):
        n = int(input())
        st = list(map(int, input().split()))
        count = 0
        prev = 0

        for i in st:
            if prev > i:
                count += (prev - 1) - i
                prev = i
            else:
                count += (i - 1) - prev
                prev = i

        print(count)

except EOFError:
    pass
