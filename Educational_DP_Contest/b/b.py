def chmin(a, b):
    if a > b:
        return b
    return a


N, K = map(int, input().split())
H = list(map(int, input().split()))

INF_INT = 10**18

dp = [INF_INT for _ in range(N)]
dp[0] = 0

for i in range(0, N):
    for j in range(1, K + 1):
        if i + j < N:
            dp[i + j] = chmin(dp[i + j], dp[i] + abs(H[i] - H[i + j]))
print(dp[N - 1])
