def d_int(m1, n1):
    return m1 ^ n1


if __name__ == "__main__":
    m1st = int(input())
    m2nd = set(list(map(int,input().split())))

    n1st = int(input())
    n2nd = set(list(map(int,input().split())))

    diff_int =list( d_int(m2nd, n2nd))
    diff_int.sort()
    for i in diff_int:
        print(i)