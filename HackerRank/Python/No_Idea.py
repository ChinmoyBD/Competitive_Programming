def count(arr, n1, n2):
    co = 0
    for i in arr:
        if i in n1:
            co += 1
        if i in n2:
            co -= 1

    return co

if __name__ == "__main__":
    n, m = map(int,input().split())
    arr = list(map(int,input().split()))
    n1 = set(map(int, input().split()))
    n2 = set(map(int, input().split()))
    result = count(arr, n1, n2)
    print(result)