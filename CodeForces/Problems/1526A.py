# for _ in range(int(input())):
#     n = int(input())
#     arr = list(map(int, input().split()))
#
#     arr.sort()
#     for i in range(n):
#         if i != n-1:
#             print(arr[i], arr[n+i], end=' ')
#         else:
#             print(arr[i], arr[n+i])

def romanToInteger(s: str) -> int:
    rToI = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    pre = rToI[s[0]]
    ans = 0
    ck = 0
    le_n = len(s)
    for i in s:
        if ck == 0:
            ck += 1
            continue
        if rToI[i] <= pre:
            ans += pre
            if le_n == ck+1:
                ans += rToI[i]
        else:
            ans += rToI[i] - pre
        pre = rToI[i]
        ck += 1
    return ans


print(romanToInteger('MCMXCIV'))