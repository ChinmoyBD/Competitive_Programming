n, k = map(int, input().split())
s = input()
i = 1
while s[i:] != s[:-i]:
    i += 1
print((s[:i]*k) + s[i:])

"""
n,k=map(int,input().split())
t=input()
i=1
while t[i:]!=t[:-i]:i+=1
print(t[:i]*k+t[i:])
"""