def climbingLeaderboard(scores, alice):
    rank = []
    for i in alice:
        scores.append(i)
        scores = list(reversed(sorted(set(scores))))

        rank.append(scores.index(i)+1)

    return rank


if __name__ == "__main__":
    scores_count = int(input())

    scores = list(map(int,input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    print(climbingLeaderboard(scores, alice))