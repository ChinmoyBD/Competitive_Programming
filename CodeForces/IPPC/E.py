def rec(arr):
    if not arr:
        return 0
    else:
        return arr[0] + rec(arr[1:])


for i in range(int(input())):
    arr = list(map(int, input().split()))[1:]
    print('Case %d: %d'%(i+1, rec(arr)))