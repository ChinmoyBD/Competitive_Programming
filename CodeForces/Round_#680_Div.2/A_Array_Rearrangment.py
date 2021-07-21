t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    i_n = 1
    for i in range(n):
        if a[i] + b[n-i_n] > x:
            print("NO")
            break
        i_n += 1
    else:
        print("YES")
    if _ != t-1:
        input()