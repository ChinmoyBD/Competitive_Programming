n = int(input())
st = input().lower()

count = len(set(st))

if count == 26:
    print("YES")
else:
    print("NO")