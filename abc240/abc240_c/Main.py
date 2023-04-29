N, X = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(N)]

dp = [[False] * (X+1) for _ in range(N+1)]
dp[0][0] = True
for i in range(1, N+1):
    for j in range(X+1):
        if j - ab[i-1][0] >= 0 and dp[i-1][j - ab[i-1][0]]:
            dp[i][j] = dp[i-1][j - ab[i-1][0]]
        if j - ab[i-1][1] >= 0 and dp[i-1][j - ab[i-1][1]]:
            dp[i][j] = dp[i-1][j - ab[i-1][1]]
if dp[N][X]:
    print("Yes")
else:
    print("No")