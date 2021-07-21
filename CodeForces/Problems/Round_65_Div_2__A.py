t = int(input())
for _ in range(t):
    s = input().strip()

    le_n = len(s)

    if le_n > 10:
        print(f"{s[0]}{le_n-2}{s[-1]}")
    else:
        print(s)