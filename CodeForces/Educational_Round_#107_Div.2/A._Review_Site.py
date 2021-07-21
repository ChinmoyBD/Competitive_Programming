for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    upVotes1 = downVotes1 = 0
    upVotes2 = downVotes2 = 0

    server1 = server2 = 0
    for i in arr:
        if i == 1:
            if upVotes1 > upVotes2:
                upVotes1 += 1
            else:
                upVotes2 += 1
        elif i == 2:
            if downVotes1 > downVotes1:
                downVotes1 += 1
            else:
                downVotes2 += 1
        else:
            if upVotes1 >= downVotes1 or upVotes2 >= downVotes2:
                if (upVotes2 >= downVotes2) and (upVotes2 > upVotes1):
                    upVotes2 += 1
                else:
                    upVotes1 += 1
            else:
                if downVotes1 > downVotes1:
                    downVotes1 += 1
                else:
                    downVotes2 += 1

    print(upVotes2+upVotes1)

