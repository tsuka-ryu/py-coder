def get_all_splits(s):
    n = len(s)
    results = []

    for bit in range(1 << (n - 1)):
        parts = []
        start = 0
        for i in range(n - 1):
            if bit & (1 << i):
                parts.append(int(s[start : i + 1]))
                start = i + 1
        parts.append(int(s[start:]))
        results.append(parts)

    return results


# 文字列の全ての分割パターンを作って、加算するのほうがシンプルな気がする
S = input()

ans = 0
for split in get_all_splits(S):
    ans += sum(split)

print(ans)
