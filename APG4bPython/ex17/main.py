N, M = map(int, input().split())
AB = [list(map(int, input().split())) for i in range(M)]
# ここにコードを追記する

R = [["-"] * N for _ in range(N)]

for a, b in AB:
    R[a - 1][b - 1] = "o"
    R[b - 1][a - 1] = "x"

for i in R:
    print(*i)
