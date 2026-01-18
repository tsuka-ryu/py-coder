S, T = map(str, input().split())

INF_INT = 10**18

dp = [[INF_INT] * (len(T) + 1) for _ in range(len(S) + 1)]
dp[0][0] = 0


def chmin(a, b):
    if a > b:
        return b
    return a


for i in range(len(S) + 1):
    for j in range(len(T) + 1):
        # 変更操作（または一致）
        if i > 0 and j > 0:
            if S[i - 1] == T[j - 1]:
                dp[i][j] = chmin(dp[i][j], dp[i - 1][j - 1])
            else:
                dp[i][j] = chmin(dp[i][j], dp[i - 1][j - 1] + 1)

        # 削除操作
        if i > 0:
            dp[i][j] = chmin(dp[i][j], dp[i - 1][j] + 1)

        # 挿入操作
        if j > 0:
            dp[i][j] = chmin(dp[i][j], dp[i][j - 1] + 1)

print(dp[len(S)][len(T)])

# 編集距離の動的計画法
# 他の動的計画法もそうだけど、
# 更新操作が3種類あって、その中で一番いいものがdp[i][j]に残っていく、みたいなイメージな気がしてきた
