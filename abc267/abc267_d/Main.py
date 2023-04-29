N, M = map(int, input().split())
A = list(map(int, input().split()))

## N, M 2*10^3
dp = [[-10**18] * (M + 1)  for _ in range(N+1)]
for i in range(N + 1):
    dp[i][0] = 0


for i in range(1, N + 1):
    for j in range(M + 1):
        if j == 0:
            dp[i][j] = 0
        elif i >= j:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + (j * A[i - 1]))

print(dp[N][M])
