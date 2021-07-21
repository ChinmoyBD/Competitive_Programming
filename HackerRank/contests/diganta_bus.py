s, t = map(int, input().split())
sh = s*2
hl = s*3

if (sh <= t) and (hl >= t):
    print("{}tk".format(0))
elif hl < t:
    print("{}tk".format(t-hl))