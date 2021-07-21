for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    count = 0
    dic = dict()

    for i in range(n):
        res = arr[i] - i

        try:
            dic[res] += 1
        except KeyError:
            dic[res] = 1
    for x in dic.values():
        count += (x*(x-1)) // 2
    print(count)