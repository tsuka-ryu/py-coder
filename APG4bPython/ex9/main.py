N = int(input())
A = int(input())
# ここにプログラムを追記

for i in range(N):
    op, B = input().split()
    B = int(B)

    if op == "+":
        A = A + B
    elif op == "-":
        A = A - B
    elif op == "*":
        A = A * B
    elif op == "/":
        if B == 0:
            print("error")
            break
        else:
            A = A // B

    print(i + 1, A)
