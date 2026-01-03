# 例: 配列の全ての部分集合を列挙
arr = ["A", "B", "C", "D"]
N = len(arr)

for bit in range(1 << N):  # 2^N 通り
    subset = []
    for i in range(N):
        if bit & (1 << i):  # i番目のビットが1か?
            subset.append(arr[i])
    print(subset)
