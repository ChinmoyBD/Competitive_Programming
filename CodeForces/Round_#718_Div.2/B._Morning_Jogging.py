from collections import deque


def check(li):
    inMin = li[0][0]
    index = 0
    for i in range(len(li)):
        if inMin > li[i][0]:
            inMin = li[i][0]
            index = i
    return index


for _ in range(int(input())):
    n, m = map(int, input().split())
    arr = deque()
    for x in range(n):
        tArr = list(map(int, input().split()))
        arr.append(deque(sorted(tArr)))

    rArr = [[-1 for j in range(m)] for i in range(n)]
    for i in range(m):
        index = check(arr)
        for j in range(n):
            if index == j:
                rArr[j][i] = arr[j].popleft()
            else:
                rArr[j][i] = arr[j].pop()

    # print
    for r in rArr:
        print(*r)
