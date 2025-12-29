N, K = map(int, input().split())

S = input().split()

ans = [x for x in S if len(x) >= K]

# *ansにすると、空リストのとき、空行になる
# if len(ans) == 0:
#     print()
# else:
#     print(*ans)

print(*ans)
