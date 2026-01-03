K, N = map(int, input().split())

count = 0
# 三重ループするとO(K^3）になるが、二重ループで十分
for x in range(K + 1):
    for y in range(K + 1):
        z = N - x - y
        print(x, y, z)
        if z >= 0 and z <= K:
            count += 1

print(count)
