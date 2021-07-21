def printLatin(n):

    k = n + 1
    li = []
    for i in range(1, n + 1, 1):
        l = []
        temp = k
        while temp <= n:
            l.append(temp)
            # print(temp, end=" ")
            temp += 1

        for j in range(1, k):
            # print(j, end=" ")
            l.append(j)

        li.append(l)
        k -= 1
        # print()

    print(li)


printLatin(3)
