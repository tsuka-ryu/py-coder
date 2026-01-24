MOD = 1000000007

N, M = map(int, input().split())
a = [0] * M


def chmax(a, b):
    if a < b:
        return b
    return a


for i in range(M):
    a[i] = int(input())

dp = [0] * (N + 1)
dp[0] = 1  # 0段目にいる方法は1通り

# 壊れている足場をセットに変換（高速化）
broken = set(a)

for i in range(1, N + 1):
    # i段目が壊れている場合は到達不可能
    if i in broken:
        continue

    # 1段前から来る方法
    dp[i] = dp[i - 1]

    # 2段前から来る方法（i >= 2 の場合）
    if i >= 2:
        dp[i] = (dp[i] + dp[i - 2]) % MOD

print(dp[N])
