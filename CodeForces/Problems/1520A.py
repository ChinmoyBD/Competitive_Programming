for _ in range(int(input())):
    n = int(input())
    st = input().strip().upper()

    stArr = [False] * 26
    for i in range(n):
        ii = ord(st[i]) - 65
        if stArr[ii] is False:
            stArr[ii] = True
        else:
            if st[i] != st[i-1]:
                print("NO")
                break
    else:
        print("YES")