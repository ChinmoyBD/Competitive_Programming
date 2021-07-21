def utopianTree(li, n):
    return lihttps://join.skype.com/hy90kjqBE5wy[n]


if __name__ == "__main__":
    li = [1]
    count = 1
    for i in range(1,62):
        if i % 2 == 0:
            count += 1
            li.append(count)
        else:
            count *= 2
            li.append(count)

    for _ in range(int(input())):
        n = int(input())

        print(utopianTree(li, n))