def separateNumbers(s):
    l = len(s)
    for i in range(1, l//2 + 1):
        ss = s[:i]
        n = int(ss)
        while len(ss) < l:
            n += 1
            ss += str(n)
        if ss == s:
            return f"YES {s[:i]}"
    return "NO"


if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()

        print(separateNumbers(s))
