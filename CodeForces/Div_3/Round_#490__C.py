n, k = map(int, input().split())
st = list(input())

if n != k:
    for ch in range(97, 123):
        if k <= 0:
            break
        i = 0
        ch = chr(ch)
        while n > i:
            if ch == st[i] and k > 0:
                st[i] = ''
                k -= 1
            else:
                i += 1
            if k <= 0:
                break
    print("".join(st))
else:
    print('')

