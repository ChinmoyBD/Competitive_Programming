def runner_up(arr):
    set_list = set(arr)
    li = list(set_list)
    ma = max(li)
    for i in range(len(li)):
        if li[i] == ma:
            del(li[i])
            break
    r = max(li)
    return r
if __name__ == "__main__":
    n = int(input())
    arr = list(map(int,input().split()))
    r_u = runner_up(arr)
    print(r_u)