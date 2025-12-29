N = int(input())
A = list(map(int, input().split()))

sum = 0

for i in A:
    sum += i

avr = sum // N

for i in range(len(A)):
    print(abs(A[i] - avr))
