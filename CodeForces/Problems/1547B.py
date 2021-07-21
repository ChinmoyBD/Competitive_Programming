for _ in range(int(input())):
    st = input()
    stLen = len(st)
    left = right = -1
    ck = True
    for a in range(stLen):
        if st[a] == 'a':
            left = right = a
            break
    if left >= 0:
        for i in range(1, stLen):
            if right < stLen-1 and ord(st[right+1]) - 97 == i:
                right += 1
            elif left > 0 and ord(st[left-1]) - 97 == i:
                left -= 1
            else:
                ck = False
                break
    if ck and left >= 0:
        print("YES")
    else:
        print("NO")
