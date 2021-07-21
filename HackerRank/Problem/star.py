n = int(input())
nn = n+n
width = n
for i in range(1, nn+1, 2):
    if i > n:
        i = nn - i
    star = '*'*i
    print(star.center(width, ' '))

