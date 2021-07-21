import math


def sqr_number(l, r):
    count = 0
    for i in range(l, r + 1):
        sqr = math.sqrt(i)
        if sqr % int(sqr) == 0:
            count += 1

    return count


if __name__ == "__main__":
    lr = input().split()

    l = int(lr[0])

    r = int(lr[1])

    print(sqr_number(l, r))
