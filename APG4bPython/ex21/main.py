A, B = map(int, input().split())

for x in range(256):
    if A ^ x == B:
        print(x)
        break
