def alternate(s):
    se = list(set(s))
    arr = []
    le = len(se)
    if le < 2:
        return 0

    for i in range(le-1):
        for j in range(i+1, le):
            arr.append([se[i], se[j]])
    ma_x = 0
    l = len(s)
    for sli in arr:
        count = 0
        temp = t = ''
        for ss in range(l):
            if (s[ss] == sli[0] or s[ss] == sli[1]) and s[ss] == temp:
                count = 0
                break
            if (s[ss] == sli[0] or s[ss] == sli[1]) and ((ss+1 != l) and s[ss+1] == s[ss]):
                count = 0
                break
            if (s[ss] == sli[0] or s[ss] == sli[1]) and s[ss] != temp:
                if (ss+1 != l) and s[ss+1] != s[ss]:
                    count += 1
                if ss + 1 == l:
                    count += 1
                if t == s[ss]:
                    count = 0
                    break
                t = s[ss]
            temp = s[ss]
        if count > ma_x:
            ma_x = count
    return ma_x


if __name__ == '__main__':
    l = int(input())
    s = input()
    print(alternate(s))