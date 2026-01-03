def fibo(N):
    # ベースケース
    if N == 0:
        return 0
    elif N == 1:
        return 1

    # メモをチェック（すでに計算済みなら答えをリターン）
    if memo[N] != -1:
        return memo[N]

    # 答えをメモ化しながら、再帰呼び出し
    memo[N] = fibo(N - 1) + fibo(N - 2)
    return memo[N]


# メモ化用配列を -1 で初期化
memo = [-1 for _ in range(50)]

# fibo(49)を呼び出す
fibo(49)

# memo[0], ..., memo[49]に答えが格納さている
for N in range(2, 50):
    print(f"{N} 項目: {memo[N]}")
