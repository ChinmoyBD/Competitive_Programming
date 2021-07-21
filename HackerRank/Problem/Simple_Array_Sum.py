def Li_sum(li):
    li_s = sum(li)
    return li_s

if __name__ == "__main__":
    n = int(input())
    li = list(map(int,input().split()))
    print(Li_sum(li))