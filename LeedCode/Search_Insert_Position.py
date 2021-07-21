def searchInsert(nums, target) -> int:
    index = 0
    for i in nums:
        if target <= i:
            return index
        index += 1

    return index


if __name__ == "__main__":
    li = list(map(int, input().split()))
    target = int(input())

    print(searchInsert(li, target))