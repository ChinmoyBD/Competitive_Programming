def bigSorting(unsorted):
    sor = unsorted.sort(key=int)

    return sor

    
if __name__ == "__main__":
    n = int(input())

    unsorted = []

    for _ in range(n):
        unsorted_item = input()
        unsorted.append(unsorted_item)

    print(bigSorting(unsorted))