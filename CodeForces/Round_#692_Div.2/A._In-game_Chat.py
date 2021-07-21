for _ in range(int(input())):
    n = int(input())
    s = input().rstrip(')')
    if len(s) < n/2:
        print("YES")
    else:
        print("NO")