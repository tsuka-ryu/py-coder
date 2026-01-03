S = input()
N = len(S)


res = 0

# N-1 箇所の隙間に「+」を入れるかどうかをすべて試す
for bit in range(1 << (N - 1)):
    # tmp：「+」と「+」との間の値を表す変数
    tmp = 0
    print(format(bit, "04b"))
    for i in range(N - 1):
        print(f"1.{tmp = }")
        tmp *= 10  # 一個前の値の桁を繰り上げる
        tmp += int(S[i])
        # 「+」を挿入するとき、答えに tmp を加算して、tmp を 0 に初期化
        if bit & 1 << i:
            print(f"2.{tmp = }")
            print(f"3.{res = }")
            res += tmp
            tmp = 0
    # 最後の「+」から残りの部分を答えに加算
    print(f"4.{tmp = }")
    tmp *= 10
    tmp += int(S[-1])
    res += tmp
    print(f"5.{res = }")

print(res)

# 賢すぎて自分で実装できる気がしないな
# tmpが状態管理みたいになってるイメージで、条件に合致した時だけ tmp=0 でクリアする
# たぶん、この解法じゃなくて、文字列の全ての組み合わせを作れば良い気がする
