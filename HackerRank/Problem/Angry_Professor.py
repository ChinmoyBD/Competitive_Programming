def angryProfessor(k, a):
    for i in a:
        if i <= 0:
            k -= 1
        if k == 0:
            return "NO"
    else:
        return "YES"


if __name__ == "__main__":
    for _ in range(int(input())):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        a = list(map(int, input().rstrip().split()))

        print(angryProfessor(k, a))
