MOD = 1000000007

N, M = map(int, input().split())
broken = set()
for _ in range(M):
    broken.add(int(input()))

dp = [0] * (N + 1)
dp[0] = 1
if 1 not in broken:
    dp[1] = 1

for i in range(2, N + 1):
    if (i - 1) not in broken:
        dp[i] += dp[i - 1]
    if (i - 2) not in broken:
        dp[i] += dp[i - 2]
    dp[i] %= MOD

print(dp[N])
print(*dp)
