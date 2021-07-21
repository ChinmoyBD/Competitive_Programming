test_case = int(input())
count = 0

for _ in range(test_case):
    operation = input().strip()

    if operation == "++X" or operation == "X++":
        count += 1
    if operation == "--X" or operation == "X--":
        count -= 1

print(count)