t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    print((n-s.count('10') - s.count('01')) // 2)
