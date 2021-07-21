t = int(input())
for _ in range(1, t+1):
    s = input().strip()
    ss = ''
    left = 0
    right = 0
    for i in s:
        m = int(i)
        if left < m:
            ss += '('*(m - left)
            left = m
            ss += i

        else:
            ss += ')'*(left - m)
            left -= left - m
            ss += i

    ss += ')'*left

    print("Case #{}: {}".format(_, ss))