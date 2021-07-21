t = int(input())
for _ in range(t):
    l, r = map(int, input().split())
    if r / 2 < l:
        print(r)
    else:
        print(-1)