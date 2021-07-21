def Latin(n):

    k = n + 1
    li = []
    for i in range(1, n + 1, 1):
        l = []
        temp = k
        while temp <= n:
            l.append(temp)

            temp += 1

        for j in range(1, k):
            l.append(j)

        li.append(l)
        k -= 1
    return li


if __name__ == "__main__":
    t = int(input())
    for _ in range(1, t+1):
        n, k = map(int, input().split())
        l = Latin(n)

        co = 0
        co_sum = 0
        for i in l:
            co_sum += i[co]
            co += 1
        if co_sum == k:
            print("Case #{}: POSSIBLE".format(_))
            for i in l:
                print(*i)

        else:
            l = l[::-1]
            co = 0
            co_sum = 0
            for i in l:
                co_sum += i[co]
                co += 1
            if co_sum == k:
                print("Case #{}: POSSIBLE".format(_))
                for i in l:
                    print(*i)
            else:
                print("Case #{}: IMPOSSIBLE".format(_))
