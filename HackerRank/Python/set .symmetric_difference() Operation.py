e = int(input())
err = set(map(int, input().split()))
f = int(input())
frr = set(map(int, input().split()))

print(len(err ^ frr))