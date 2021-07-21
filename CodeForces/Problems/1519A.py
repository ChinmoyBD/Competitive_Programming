for _ in range(int(input())):
    r, b, d = map(int, input().split())
    sev = r-b
    if sev < 0:
        sev -= sev*2

    if sev <= d:
        print("YES")
    elif (d == 0 and r != b) or ((r == 1 or b == 1) and sev > d):
        print("NO")
    else:
        if r < b:
            r, b = b, r
        if (r/b)-1 <= d:
            print("YES")
        else:
            print("NO")