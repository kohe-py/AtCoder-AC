N = int(input())
A = list(map(int, input().split()))
 
dp = [[0] * N for _ in range(N) ]
sum_a = [[0] * N for _ in range(N) ]
 
for i in range(N):
    sum_a[i][i] = A[i]
    for j in range(i+1,N):
         sum_a[i][j] = sum_a[i][j-1] + A[j]
for i in range(1,N):
    for h in range(N-i):
        t = h + i
        dp0 = 10**20
        for j in range(i):
            dp0 = min(dp0, (dp[h][h+j] + dp[h+j+1][t] + sum_a[h][t]) )
        dp[h][t] = dp0

print(dp[0][N-1])