m, s = map(int, input().split())

if s == 0 and m == 1:
    print(0, 0)
elif s == 0:
    print(-1, -1)
else:
    if s > m * 9:
        print(-1, -1)
    else:
        ma_x = str('9' * (s//9))
        if len(ma_x) < m:
            ma_x += str(s % 9)
        ma_x += '0'*(m - len(ma_x))
        mi_n = ''
        ck = False
        for i in range(m-1, -1, -1):
            if i == m-1 and ma_x[i] == '0':
                mi_n += '1'
                ck = True
            else:
                if ck and ma_x[i] != '0':
                    mi_n += str(int(ma_x[i]) - 1)
                    ck = False
                else:
                    mi_n += ma_x[i]
        print(mi_n, ma_x)
