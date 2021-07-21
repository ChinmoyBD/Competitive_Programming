def leftRotation(d, a):
    for _ in range(d):
        left_i = a.pop(0)
        a.append(left_i)

    return a


if __name__ == "__main__":
    nd = input().split()

    d = int(nd[1])

    a = list(map(int, input().split()))

    print(*leftRotation(d, a),sep=' ')