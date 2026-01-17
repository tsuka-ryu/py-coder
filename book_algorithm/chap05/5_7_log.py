import sys


def chmax(a, b):
    if a < b:
        return b
    return a


N, W = map(int, input().split())
weight = [0] * N
value = [0] * N
for i in range(N):
    weight[i], value[i] = map(int, input().split())

# ログファイルを開く
log_file = open("dp_log.txt", "w", encoding="utf-8")
original_stdout = sys.stdout

# DPテーブル定義
# dp[i][w] = i番目までの品物から重さwを超えないように選んだ時の価値の最大値
dp = [[0] * (W + 1) for _ in range(N + 1)]


def print_dp_table():
    output = "\n【DPテーブル全体】\n"
    output += "    "
    for w in range(W + 1):
        output += f"w={w:2} "
    output += "\n"
    for i in range(N + 1):
        output += f"i={i}: "
        for w in range(W + 1):
            output += f"{dp[i][w]:3} "
        output += "\n"
    print(output, end="")
    log_file.write(output)


# 初期状態を表示
msg = "=== 初期状態 ===\n"
print(msg, end="")
log_file.write(msg)
print_dp_table()

# DPループ
for i in range(N):
    for w in range(W + 1):
        msg = f"\n--- 品物{i} (重さ={weight[i]}, 価値={value[i]}), 容量w={w} ---\n"
        print(msg, end="")
        log_file.write(msg)

        # i番目の品物を選ぶ場合
        if w - weight[i] >= 0:
            old_val = dp[i + 1][w]
            new_val = (
                dp[i][w - weight[i]] + value[i]
            )  # [w- weight[i]]が分かってなかったかもしれない、これがあるから容量を満たすだけの前の分の値を取ってこれる
            dp[i + 1][w] = chmax(dp[i + 1][w], new_val)

            if dp[i + 1][w] == new_val and new_val > old_val:
                msg = f"  ✓ 品物{i}を選択: dp[{i + 1}][{w}] = {dp[i + 1][w]} (前の値={old_val}, 選んだ価値={new_val})\n"
            else:
                msg = f"  × 品物{i}を選んでも改善なし: 現在値={old_val}, 選んだ場合={new_val}\n"
            print(msg, end="")
            log_file.write(msg)
            print_dp_table()
        else:
            msg = f"  - 品物{i}は重すぎて選べない (重さ{weight[i]} > 容量{w})\n"
            print(msg, end="")
            log_file.write(msg)

        # i番目の品物を選ばない場合
        # この処理は毎回実行される、if文の後にこっちで値が書き変わることもある
        old_val = dp[i + 1][w]
        dp[i + 1][w] = chmax(dp[i + 1][w], dp[i][w])

        if dp[i + 1][w] != old_val:
            msg = f"  ○ 品物{i}を選ばない方が良い: dp[{i + 1}][{w}] = {dp[i + 1][w]} (前の値={old_val})\n"
        else:
            msg = f"  = 最終的に dp[{i + 1}][{w}] = {dp[i + 1][w]}\n"
        print(msg, end="")
        log_file.write(msg)

        # 更新後のテーブルを表示
        print_dp_table()

# 最適値の出力
result = f"{dp[N][W]}\n"
print(result, end="")
log_file.write(result)

# ログファイルを閉じる
log_file.close()
print("\nログを dp_log.txt に出力しました", file=original_stdout)
