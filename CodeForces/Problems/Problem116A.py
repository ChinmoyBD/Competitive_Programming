max_pass = 0
passengers = 0
for _ in range(int(input())):
    a, b = map(int, input().split())
    passengers -= a
    passengers += b

    if passengers > max_pass:
        max_pass = passengers
print(max_pass)