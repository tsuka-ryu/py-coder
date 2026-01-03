# 例: 配列の全ての部分集合を列挙
arr = ["A", "B", "C", "D"]
N = len(arr)

for bit in range(1 << N):  # 2^N 通り
    subset = []
    for i in range(N):
        if bit & (1 << i):  # i番目のビットが1か?
            subset.append(arr[i])
    print(subset)


# 文字列のすべての分割パターンを返す
def get_all_splits(s):
    n = len(s)
    results = []

    for bit in range(1 << (n - 1)):
        parts = []
        start = 0
        for i in range(n - 1):
            if bit & (1 << i):
                parts.append(s[start : i + 1])
                start = i + 1
        parts.append(s[start:])
        results.append(parts)

    return results
