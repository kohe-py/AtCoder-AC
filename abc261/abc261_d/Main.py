N,M = map(int,input().split())
X = list(map(int, input().split()))
B= [0] * (N+1)
for i in range(M):
    c,y = map(int, input().split())
    B[c] = y


dp = [[-1]*(N+1) for i in range(N+1)]
for i in range(N+1):
    dp[0][i] =0
dp[1][1] = X[0]


for i in range(N):
    dp[i+1][0] = max(dp[i])
    for j in range(i+1):          
        dp[i+1][j] = max(dp[i][j-1] + X[i] + B[j],dp[i+1][j])
        dp[i+1][j+1] = dp[i][j] + X[i] + B[j+1]

print(max(dp[N]))