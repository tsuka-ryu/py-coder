N = int(input())
H = list(map(int, input().split()))

INF_INT = 10**18

dp = [INF_INT for _ in range(N)]
dp[0] = 0

for i in range(1, N):
    if i == 1:
        dp[1] = abs(H[i] - H[i - 1])
    else:
        dp[i] = min(dp[i - 1] + abs(H[i] - H[i - 1]), dp[i - 2] + abs(H[i] - H[i - 2]))

print(dp[N - 1])
