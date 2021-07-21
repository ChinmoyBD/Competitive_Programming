for _ in range(int(input())):
    L, u, l, r = map(int, input().split())
    print(L // u - r // u + (l - 1) // u)