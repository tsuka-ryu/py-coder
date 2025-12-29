N, S = map(int, input().split())

A = list(map(int, input().split()))
P = list(map(int, input().split()))

# リンゴ・パイナップルをそれぞれ1つずつ購入するとき合計S円になるような買い方が何通りあるか
# ここにプログラムを追記

ans = 0

for i in A:
    for j in P:
        sum = i + j
        if sum == S:
            ans += 1

print(ans)
