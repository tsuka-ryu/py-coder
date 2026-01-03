# === AtCoder 入力パターン集 ===

# 1整数
N = int(input())

# 複数整数
A, B = map(int, input().split())

# 配列
A = list(map(int, input().split()))

# 二次元配列
N, M = list(map(int, input().split()))
## 要素がない場合
a = [list(map(int, input().split())) for _ in range(N)]
## 要素がある場合
AB = [list(map(int, input().split())) for i in range(M)]
AB = [tuple(map(int, input().split())) for i in range(N)]

# 要素がすべて0の二次元配列
N, M = list(map(int, input().split()))
a = [[0] * M for _ in range(N)]

# 三次元配列
N, M, D = list(map(int, input().split()))
lst3d = [[[0] * D for _ in range(M)] for _ in range(N)]

# N×0 の二次元配列
N = int(input())
a = [[] for _ in range(N)]

# グリッド
H, W = map(int, input().split())
S = [input().strip() for _ in range(H)]

# グラフ
N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]
