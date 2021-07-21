from itertools import permutations


def it_permutations(s, k):
    so = sorted(s)
    p_li = list(permutations(so, k))
    for i in p_li:
        re = ''
        for j in i:
            re += j
        print(re)


if __name__ == "__main__":
    string, size = input().split()
    it_permutations(string, int(size))
