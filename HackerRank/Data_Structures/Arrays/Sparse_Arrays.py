def matchingStrings(strings, queries):
    item_count = []

    for i in queries:
        item_count.append(strings.count(i))

    return item_count


if __name__ == "__main__":
    strings_count = int(input())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    print(matchingStrings(strings, queries))