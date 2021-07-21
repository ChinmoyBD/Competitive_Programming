t = int(input())
for i in range(1, t+1):
    ip1 = input()
    ip2 = input()

    ip1_li = []
    ip2_li = []
    i1 = i2 = ''

    for j in ip1:
        if j == '.':
            ip1_li.append(int(i1))
            i1 = ''
        else:
            i1 += j
    ip1_li.append(int(i1))

    for k in ip2:
        if k == '.':
            ip2_li.append(int(i2))
            i2 = ''
        else:
            i2 += k
    ip2_li.append(int(i2))
    con = True
    for b in range(4):
        if int(bin(ip1_li[b])[2:]) == ip2_li[b]:
            con = True
        else:
            con = False
            break

    if con is True:
        print("Case %d: Yes" % i)
    else:
        print("Case %d: No" % i)



