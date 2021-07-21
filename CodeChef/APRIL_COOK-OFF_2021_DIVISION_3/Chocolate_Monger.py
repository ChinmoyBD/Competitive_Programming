from collections import Counter

for _ in range(int(input())):
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))
    ck = sorted(list(Counter(arr).values()))
    le = len(ck)
    tp = le
    for i in range(le-1, -1, -1):
        if ck[i] >= x:
            x = 5
