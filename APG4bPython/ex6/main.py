A, op, B = input().split()
A = int(A)
B = int(B)

if op == "+":
    print(A + B)
elif op == "-":
    print(A - B)
elif op == "*":
    print(A * B)
elif op == "/":
    if B == 0:
        print("error")
    else:
        print(A // B)
else:
    print("error")
