def function(n):
    mid = n // 2
    even_sum = ((2+n) // 2)*mid
    if n % 2 == 1:
        mid += 1
    odd_sum = ((1+n) // 2)*mid

    print(even_sum - odd_sum)


if __name__ == "__main__":
    n = int(input())
    function(n)