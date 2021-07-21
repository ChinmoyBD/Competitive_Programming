for _ in range(int(input())):
    n, m = map(int, input().split())
    ai = list(map(int, input().split()))
    bi = list(map(int, input().split()))
    swaps = a_sum = b_sum = 0
    for i in range(n if n > m else m):
        if i < n:
            a_sum += ai[i]
        if i < m:
            b_sum += bi[i]
    if a_sum <= b_sum:
        ai.sort()
        bi.sort()
        for j in range(n if n < m else m):
            if bi[-(j + 1)] > ai[j]:
                a_sum += bi[-(j + 1)]
                a_sum -= ai[j]
                b_sum += ai[j]
                b_sum -= bi[-(j + 1)]
                swaps += 1
            if a_sum > b_sum:
                break
    if a_sum > b_sum:
        print(swaps)
    else:
        print(-1)