N, X = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(N)]

result = []
s = 0
for i in range(N):
    if X <= 1:
        break
    s += ab[i][0] + ab[i][1]
    X -= 1
    result.append(s + (ab[i][1] * X))
print(min(result))