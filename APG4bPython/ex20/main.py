N = int(input())
A = list(map(int, input().split()))

d = {}

for x in A:
    if x in d:
        d[x] += 1
    else:
        d[x] = 1

key = A[0]

for x in A:
    if d[key] < d[x]:
        key = x

print(key, d[key])
