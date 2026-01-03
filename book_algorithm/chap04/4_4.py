def GCD(m, n):
    # ベースケース
    if n == 0:
        return m
    # 再帰呼び出し
    return GCD(n, m % n)


print(GCD(51, 15))
