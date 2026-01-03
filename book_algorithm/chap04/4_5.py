def fibo(N):
    # 再帰関数を呼び出したことを報告する
    print(f"fib({N})を呼び出しました")

    # ベースケース
    if N == 0:
        return 0
    elif N == 1:
        return 1

    # 再帰的に答えを求めて出力する
    result = fibo(N - 1) + fibo(N - 2)
    print(f"{N} 項目 = {result}")

    return result


fibo(6)
