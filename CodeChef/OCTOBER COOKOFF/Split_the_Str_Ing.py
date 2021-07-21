t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    b = ''
    mid = n//2
    i_i = mid
    a = s[:mid]
    check = False
    for i in range(mid, n):
        b = s[i_i:]
        if b in a:
            check = True
            break
        a += s[i]
        i_i += 1
    if check:
        print("YES")
    else:
        print("NO")