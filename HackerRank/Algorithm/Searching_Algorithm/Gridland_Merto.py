def gridlandMetro(n, m, track):
    track.sort()
    nm = n * m
    sn = track[0][0]
    s = (track[0][2] - track[0][1]) + 1

    for i in track:
        if sn != i[0]:
            nm -= s
            s = (i[2] - i[1]) + 1
            sn = i[0]

        co = (i[2] - i[1]) + 1
        if co > s:
            s = co
    nm -= s

    return nm


if __name__ == "__main__":
    nmk = input().split()

    n = int(nmk[0])

    m = int(nmk[1])

    k = int(nmk[2])

    track = []

    for _ in range(k):
        track.append(list(map(int, input().split())))

    print(gridlandMetro(n, m, track))