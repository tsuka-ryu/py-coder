N = int(input())

AB = [tuple(map(int, input().split())) for i in range(N)]

AB.sort(key=lambda x: x[1])

for i in range(N):
    print(*AB[i])
