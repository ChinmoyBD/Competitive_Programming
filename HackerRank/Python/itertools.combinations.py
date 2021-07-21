from itertools import combinations


def it_combinations(s, k):
    so = sorted(set(s))
    # so = sorted(s)

    com = list(combinations(so, k))
    for i in so:
        print(i)
    for i in com:
        st = ''
        for j in i:
            st += j
        print(st)


if __name__ == "__main__":
    string, size = input().upper().strip().split()
    it_combinations(string, int(size))
