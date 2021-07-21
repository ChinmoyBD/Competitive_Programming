for i in range(int(input())):
    li = list(map(int, input().split()))
    print("Case %d: %d" % (i+1, sum(li[1:]) // li[0]))