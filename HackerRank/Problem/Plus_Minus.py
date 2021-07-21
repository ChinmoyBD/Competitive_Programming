
def plusMinus(arr):
    la = len(arr)
    positive = 0
    negative = 0
    zero = 0
    for i in arr:
        if i > 0:
            positive += 1
        elif i < 0:
            negative += 1
        else:
            zero += 1
    li = [positive, negative, zero]
    for i in li:
        b = i / la
        print("{0:.6f}".format(b))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
