def how_many_times(a):
    exp = 0
    while a % 2 == 0:
        # print(f"{a = }")
        a //= 2
        exp += 1
    # print(f"{exp = }")
    return exp


N = int(input())
A = list(map(int, input().split()))

result = 10**18

for i in A:
    result = min(result, how_many_times(i))

print(result)
