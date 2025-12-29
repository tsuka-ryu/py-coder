data = [int(c) for c in input().split()]
# dataの中で隣り合う等しい要素が存在するなら"YES"を出力し、そうでなければ"NO"を出力する
# ここにプログラムを追記
for a, b in zip(data, data[1:]):
    if a == b:
        print("YES")
        break
else:
    print("NO")
