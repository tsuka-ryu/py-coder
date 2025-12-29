N = int(input())  # 生徒の数Nを読み込む
T = list(map(int, input().split()))  # 各生徒のゴールまでの時間を読み込む

min = min(T)

ans = T.index(min)

print(ans + 1)
