for _ in range(int(input())):
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(input()))
    st1 = st2 = '.'
    st1Index = st2Index = []
    for s in range(n):
        for i in range(n):
            if arr[s][i] == "*" and st1 != "*":
                st1Index = [s, i]
                st1 = "*"
            elif arr[s][i] == "*" and st2 != "*":
                st2Index = [s, i]
                st2 = "*"
                break
        if st1 == "*" and st2 == "*":
            break
    i_n1 = st1Index[1]
    i_n2 = st2Index[1]
    if st1Index[0] == st2Index[0]:
        i_n = st1Index[0]
        if st1Index[0] < n-1:
            a = 1
        else:
            a = -1
        arr[i_n+a][i_n1] = "*"
        arr[i_n+a][i_n2] = "*"
    else:
        if st1Index[1] > st2Index[1]:
            arr[st2Index[0]][i_n1] = "*"
            arr[st1Index[0]][i_n2] = "*"
        elif st1Index[1] < st2Index[1]:
            arr[st1Index[0]][i_n2] = "*"
            arr[st2Index[0]][i_n1] = "*"
        else:
            if st1Index[1] < n - 1:
                a = 1
            else:
                a = -1
            arr[st1Index[0]][i_n1+a] = "*"
            arr[st2Index[0]][i_n2+a] = "*"

    for ai in arr:
        pr = ''
        for i in ai:
            pr += i
        print(pr)


