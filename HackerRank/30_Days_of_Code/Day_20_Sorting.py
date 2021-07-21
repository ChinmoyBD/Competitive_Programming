def bubble_sort(L):
    n = len(L)
    count = 0

    for i in range(n):
        for j in range(n-i-1):
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]
                count += 1

    return [count, L[0], L[-1]]


n = int(input())
a = list(map(int, input().strip().split(' ')))

res = bubble_sort(a)

print("Array is sorted in {} swaps.".format(res[0]))
print("First Element:", res[1])
print("Last Element:", res[2])