def viralAdvertising(n):
    cumulative = 2
    liked = 2
    for day in range(n-1):
        liked = (liked*3) // 2
        cumulative += liked

    return cumulative


if __name__ == "__main__":
    n = int(input())

    print(viralAdvertising(n))