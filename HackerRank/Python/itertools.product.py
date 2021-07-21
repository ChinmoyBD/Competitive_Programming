import itertools
from itertools import product


def it_product(a, b):
    re = list(product(a, b))
    for i in re:
        print(i,end=' ')


if __name__ == "__main__":
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))

    it_product(A, B)
