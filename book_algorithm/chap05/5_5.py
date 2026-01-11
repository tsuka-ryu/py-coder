N = int(input())
H = list(map(int, input().split()))


def chmin(a, b):
    if a > b:
        return b
    return a


def rec(i):
    # 足場 0 のコストは 0
    if i == 0:
        return 0

    res = 10**18

    #  頂点 i - 1 から来た場合
    res = chmin(res, rec(i - 1) + abs(H[i] - H[i - 1]))

    # 頂点 i - 2 から来た場合
    if i > 1:
        res = chmin(res, rec(i - 2) + abs(H[i] - H[i - 2]))

    return res
