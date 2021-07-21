def search(path, ch):
    pass


if __name__ == "__main__":
    t = int(input())
    file = []

    for case in range(1, t+1):
        n = int(input())
        for _ in range(n):

            s = input().strip()
            file.append(s)

        st = input().strip()

        for i in range(n):
            call = search(file[i], st)

            print("Case {}".format(case))
