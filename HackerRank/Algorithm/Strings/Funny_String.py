def funnyString(s):
    sl = len(s)
    asci = []
    for ss in range(sl):
        if ss != 0:
            if ord(s[ss]) > ord(s[ss - 1]):
                asci.append(ord(s[ss]) - ord(s[ss - 1]))
            else:
                asci.append(ord(s[ss - 1]) - ord(s[ss]))
    print(asci)
    for i in range(sl - 2 // 2):
        if asci[i] != asci[(sl - 2) - i]:
            return "Not Funny"
    return "Funny"


if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()
        print(funnyString(s))