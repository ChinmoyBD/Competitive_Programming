import collections

if __name__ == "__main__":
    n = int(input())
    shoe_li = list(map(int, input().split()))
    li = []
    co_shoe = collections.Counter(shoe_li).items()

    for i in co_shoe:
        li.append(list(i))
    p_sum = 0

    t = int(input())
    for _ in range(t):
        size, price = map(int, input().split())
        for i in range(len(li)):
            if li[i][0] == size:
                if li[i][1] > 0:
                    a_p = li[i][1] - 1
                    li[i][1] = a_p
                    p_sum += price
                break
    print(p_sum)
