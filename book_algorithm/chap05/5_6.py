N = int(input())
H = list(map(int, input().split()))

INF_INT = 10**18

dp = [INF_INT for _ in range(N)]


def chmin(a, b):
    if a > b:
        return b
    return a


def rec(i):
    # DPの値が更新されてたらリターン
    if dp[i] < INF_INT:
        return dp[i]

    # ベースケース
    if i == 0:
        return 0

    # 答えを表す変数
    res = INF_INT

    # 足場 i -1 から来た場合
    res = chmin(res, rec(i - 1) + abs(H[i] - H[i - 1]))

    # 足場 i - 2 から来た場合
    if i > 1:
        res = chmin(res, rec(i - 2) + abs(H[i] - H[i - 2]))

    # メモ化しながら返す
    dp[i] = res
    return res


print(rec(N - 1))
