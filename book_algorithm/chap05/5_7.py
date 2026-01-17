def chmax(a, b):
    if a < b:
        return b
    return a


N, W = map(int, input().split())
weight = [0] * N
value = [0] * N
for i in range(N):
    weight[i], value[i] = map(int, input().split())

# DPテーブル定義
# dp[i][w] = i番目までの品物から重さwを超えないように選んだ時の価値の最大値
dp = [[0] * (W + 1) for _ in range(N + 1)]

# DPループ
for i in range(N):
    for w in range(W + 1):
        # i番目の品物を選ぶ場合
        if w - weight[i] >= 0:
            dp[i + 1][w] = chmax(dp[i + 1][w], dp[i][w - weight[i]] + value[i])
            print(f"if{i, w}{dp[i + 1][w]}")

        # i番目の品物を選ばない場合
        # この処理は毎回実行される、if文の後にこっちで値が書き変わることもある
        dp[i + 1][w] = chmax(dp[i + 1][w], dp[i][w])
        print(f"else{i, w}{dp[i + 1][w]}")

# 最適値の出力
print(dp[N][W])
