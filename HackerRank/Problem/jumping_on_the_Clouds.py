def jumpingOnClouds(c, k):
    energy = 100
    n = len(c)
    i = k % n
    energy -= c[i] * 2 + 1
    while i != 0:
        i = (i+k) % n
        energy -= c[i] * 2 + 1

    return energy


if __name__ == "__main__":
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    print(jumpingOnClouds(c, k))