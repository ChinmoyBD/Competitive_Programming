n,m = map(int, input().split())
count = 0
n = n - 1
n = n*(n+1)//2
m = m*(m+1)//2

count = m - n
print("Output:", count)