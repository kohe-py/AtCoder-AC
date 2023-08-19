N = int(input())
X, Y = map(int, input().split())
A, B = [], []
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

dp = [[[400] * (Y + 1) for _ in range(X + 1)]for _ in range(N + 1)]
dp[0][0][0] = 0

for i in range(1, N + 1):
    for j in range(X + 1):
        for k in range(Y + 1):
            dp[i][j][k] = min(dp[i][j][k], dp[i - 1][j][k])
            dp[i][min(j + A[i - 1], X)][min(k + B[i - 1], Y)] = min(dp[i][min(j + A[i - 1], X)][min(k + B[i - 1], Y)], dp[i - 1][j][k] + 1)

ans = 400
for i in range(N + 1):
    ans = min(ans, dp[i][X][Y])
if ans == 400:
    print(-1)
else:
    print(ans)

