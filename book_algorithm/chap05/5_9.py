# 区間分割の最適化問題

# 入力
N = int(input())
c = []
for i in range(N + 1):
    row = list(map(int, input().split()))
    c.append(row)

INF = 10**18


def chmin(a, b):
    if a > b:
        return b
    return a


# DP テーブル定義
# dp[i] = 区間 [0, i) を分割したときの最小コスト
dp = [INF] * (N + 1)

# DP 初期条件
dp[0] = 0

# DP ループ
for i in range(N + 1):
    for j in range(i):
        # 区間 [0, i) を [0, j) と [j, i) に分割
        # dp[j]: 区間 [0, j) の最小コスト
        # c[j][i]: 区間 [j, i) のスコア
        dp[i] = chmin(dp[i], dp[j] + c[j][i])

# 答えの出力
print(dp[N])

# 区間分割の動的計画法
# dp[i]を更新するとき、最後の区間 [j, i) をどこから始めるか（jの選択）を全部試す
# その中で最小コストになるものを選ぶ
