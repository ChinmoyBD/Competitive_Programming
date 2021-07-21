def binary_search_recursive(arr, left, right, x):
    mid = (left + right) // 2

    if arr[mid][0] == x:
        return arr[mid][1]
    if arr[mid][0] < x:
        return binary_search_recursive(arr, mid+1, right, x)
    else:
        return binary_search_recursive(arr, left, mid-1, x)


n, q = map(int, input().split())

nArr = list(map(int, input().split()))
qArr = list(map(int, input().split()))

"""
arr = []
setQ = sorted(list(set(qArr)))
lenSetQ = len(setQ)


for qI in range(lenSetQ):
    for nI in range(n):
        if nArr[nI] == setQ[qI]:
            arr.append([setQ[qI], nI])
            break

cardIndArr = []
"""

for j in qArr:
    for nI in range(n):
        if j == nArr[nI]:
            cardInd = nI
            break
    print(cardInd+1, end=' ')

    for i in range(cardInd, 0, -1):
        nArr[i], nArr[i-1] = nArr[i-1], nArr[i]
