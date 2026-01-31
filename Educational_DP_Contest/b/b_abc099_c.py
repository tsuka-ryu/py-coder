def chmin(a, b):
    if a > b:
        return b
    return a


N = int(input())

INF_INT = 10**18

dp = [INF_INT for _ in range(N + 1)]
dp[0] = 0

for i in range(0, N + 1):
    if i + 1 <= N:
        dp[i + 1] = chmin(dp[i + 1], dp[i] + 1)
    for j in range(1, 6 + 1):
        m = 6**j
        if i + m <= N:
            dp[i + m] = chmin(dp[i + m], dp[i] + 1)
    for j in range(1, 5 + 1):
        m = 9**j
        if i + m <= N:
            dp[i + m] = chmin(dp[i + m], dp[i] + 1)
print(dp[N])
