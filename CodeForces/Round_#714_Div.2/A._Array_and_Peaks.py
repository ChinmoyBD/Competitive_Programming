for _ in range(int(input())):
    n, k = map(int, input().split())
    np = (n-1)//2

    if np < k:
        print(-1)
    else:
        for i in range(1, n+1):
            if i != 1 and k > 0:
                if i % 2 == 0:
                    i += 1
                else:
                    i -= 1
                    k -= 1

            print(i, end=' ')