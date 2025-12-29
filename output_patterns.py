# === AtCoder 出力パターン集 ===

# 数値、文字列
x = 0
print(x)

# スペース区切りのカンマ
print("Hello, world!", 123)

# 改行区切り、出力後の挿入文字列
print("Hello, world!", 123, sep="\n")
print("Hello, world!", end=" ")

# リストの出力
a = [9, 9, 7, 3]
print(*a)


# === f-string フォーマットチートシート ===

# サンプル値
val_float = 3.141592653589793
val_int = 42
val_negative = -123
val_large = 1234567.89

# 小数点以下の桁数を指定
print(f"{val_float:.2f}")   # 3.14
print(f"{val_float:.13f}")  # 3.1415926535898

# 指数形式にする
print(f"{val_float:e}")     # 3.141593e+00
print(f"{val_float:E}")     # 3.141593E+00

# 2進法にする
print(f"{val_int:b}")       # 101010
print(f"{val_int:#b}")      # 0b101010

# 16進法にする
print(f"{val_int:x}")       # 2a
print(f"{val_int:X}")       # 2A
print(f"{val_int:#x}")      # 0x2a

# leading zeroを含めて桁数を指定
print(f"{val_int:013}")     # 0000000000042

# 値が負でないとき先頭に + をつける
print(f"{val_int:+}")       # +42
print(f"{val_negative:+}")  # -123

# パーセンテージにする
print(f"{0.85:%}")          # 85.000000%
print(f"{0.85:.2%}")        # 85.00%

# 3桁ごとにカンマで区切る
print(f"{val_large:,}")     # 1,234,567.89
print(f"{1234567890:,}")    # 1,234,567,890

# 指定した幅に右詰め
print(f"{val_int:>13}")     # '           42'

# 指定した幅に左詰め
print(f"{val_int:<13}")     # '42           '
