t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    if sum(arr) == m:
        print("YES")
    else:
        print("NO")