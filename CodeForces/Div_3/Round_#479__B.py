n = int(input())
s = input().upper()
res = 0
ans = ''
for i in range(n-1):
    count = 0
    for j in range(n-1):
        if s[j] == s[i] and s[j+1] == s[i+1]:
            count += 1

    if res < count:
        res = count
        ans = s[i]+s[i+1]

print(ans)