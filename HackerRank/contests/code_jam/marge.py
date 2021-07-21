def merge(intervals, n):
    res = 'C'
    intervals.sort()
    Cintervals = []
    Jintervals = []
    Cintervals.append(intervals[0])

    for i in range(1, n):
        if intervals[i][0] >= Cintervals[-1][1]:
            res += 'C'
            Cintervals.append(intervals[i])
        elif len(Jintervals) == 0:  # First
            res += 'J'
            Jintervals.append(intervals[i])
        elif len(Jintervals) != 0 and intervals[i][0] >= Jintervals[-1][1]:
            res += 'J'
            Jintervals.append(intervals[i])
        else:
            return "IMPOSSIBLE"

    return res


t = int(input())
for case in range(1, t + 1):
    n = int(input())
    intervals = []
    for _ in range(n):
        s, e = [int(s) for s in input().split(" ")]
        intervals.append((s, e))
    res = merge(intervals, n)
    print("Case #{}: {}".format(case, res))