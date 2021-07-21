from collections import defaultdict


def merge(intervals):
    n = len(intervals)
    res = ''
    dd = defaultdict(str)
    noneIntervals = list(intervals)
    intervals.sort()
    Cintervals = []
    Jintervals = []
    Cintervals.append(intervals[0])
    dd[intervals[0]] += "C"

    for i in range(1, n):
        if intervals[i][0] >= Cintervals[-1][1]:
            dd[intervals[i]] += "C"
            Cintervals.append(intervals[i])
        elif len(Jintervals) == 0:
            dd[intervals[i]] += "J"
            Jintervals.append(intervals[i])
        elif len(Jintervals) != 0 and intervals[i][0] >= Jintervals[-1][1]:
            dd[intervals[i]] += "J"
            Jintervals.append(intervals[i])
        else:
            return "IMPOSSIBLE"

    for values in noneIntervals:
        res += dd[values]
        dd[values] = ''

    return res


t = int(input())
for case in range(1, t + 1):
    n = int(input())
    intervals = []
    for _ in range(n):
        s, e = [int(s) for s in input().split(" ")]
        intervals.append((s, e))
    res = merge(intervals)
    print("Case #{}: {}".format(case, res))