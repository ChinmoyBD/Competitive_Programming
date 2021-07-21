n = int(input())
country = set()

for _ in range(n):
    country.add(input().strip())

print(len(country))