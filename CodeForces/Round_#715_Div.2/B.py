for _ in range(int(input())):
    n = int(input())
    st = input().strip()
    t = m = 0
    if st.count('M') != n // 3:
        print("NO")
    else:
        ck = True
        for i in st:
            if i == 'T':
                t += 1
            else:
                t -= 1
            if t < 0:
                print("NO")
                ck = False
                break
        if ck:
            t = m = 0
            for j in range(n-1, -1, -1):
                if st[j] == 'T':
                    t += 1
                else:
                    t -= 1
                if t < 0:
                    print("NO")
                    ck = False
                    break
            if ck:
                print("YES")
