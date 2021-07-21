def senia_sum(string):
    arr = [0] * 101
    for i in string:
        if i != '+':
            arr[int(i)] += 1
    st_sum = ''
    for s in range(1, 101):
        if arr[s] > 0:
            st_sum += (str(s)+'+') * arr[s]
    print(st_sum[:-1])


if __name__ == "__main__":
    st = input()
    senia_sum(st)