for _ in range(int(input())):
    str_ = input().strip()
    a = d = 0
    b = c = e = f = 1

    for i in range(len(str_)):
        if str_[i] == "R":
            a, b = e, f

            e = a + c
            f = b + d
        else:
            c, d = e, f

            e = a + c
            f = b + d
    print("{}/{}".format(e, f))