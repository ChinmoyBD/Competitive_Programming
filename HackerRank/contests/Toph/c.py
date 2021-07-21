s = input().strip()
f = s[0]
l = s[-1]

len_ = len(s)
res = ''
for i in range(len_):
    res += f+l

print(res)