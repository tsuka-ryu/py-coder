def chmin(a, b):
    if a > b:
        return b
    return a


N = int(input())
H = list(map(int, input().split()))

INF_INT = 10**18

dp = [INF_INT for _ in range(N)]
dp[0] = 0

for i in range(0, N):
    if i + 1 < N:
        dp[i + 1] = chmin(dp[i + 1], dp[i] + abs(H[i] - H[i + 1]))
    if i + 2 < N:
        dp[i + 2] = chmin(dp[i + 2], dp[i] + abs(H[i] - H[i + 2]))
print(dp[N - 1])

# 配るDPバージョン
