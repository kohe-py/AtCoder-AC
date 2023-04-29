N, K, D = map(int, input().split())
A = list(map(int, input().split()))

dp = [[[-1] * D for _ in range(K+1)] for _ in range(N+1)]
dp[0][0][0] = 0

for i in range(N):
    for j in range(K+1):
        for k in range(D):
            if dp[i][j][k] == -1:
                continue
            else:
                if j + 1 <= K:
                    dp[i+1][j+1][(k+A[i])%D] = max(dp[i+1][j+1][(k+A[i])%D], dp[i][j][k]+A[i])
            dp[i+1][j][k] = max(dp[i+1][j][k], dp[i][j][k])
print(dp[N][K][0])