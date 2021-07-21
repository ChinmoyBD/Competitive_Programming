t = int(input())
stack = [0]
count = 0
for _ in range(t):
    item = list(map(int, input().split()))

    if item[0] == 1:
        stack.append(max(item[1], stack[-1]))

    elif item[0] == 2:
        stack.pop()
    else:
        print(stack[-1])