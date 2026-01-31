def chmin(a, b):
    if a > b:
        return b
    return a


N = int(input())
H = list(map(int, input().split()))

INF_INT = 10**18

dp = [INF_INT for _ in range(N)]
dp[0] = 0

for i in range(1, N):
    dp[i] = chmin(dp[i], dp[i - 1] + abs(H[i] - H[i - 1]))
    if i > 1:
        dp[i] = chmin(dp[i], dp[i - 2] + abs(H[i] - H[i - 2]))

print(dp[N - 1])
