N, W = map(int, input().split())
A = list(map(int, input().split()))

print(A)

exist = False
for bit in range(1 << N):
    sum = 0
    for i in range(N):
        if bit & (1 << i):
            sum += A[i]

    if sum == W:
        exist = True

if exist:
    print("Yes")
else:
    print("No")
