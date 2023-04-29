N = int(input())
 
M = 10 ** 5 + 1
X = [0] * (M+1)
A = [0] * (M+1)
 
for _ in range(N):
    t, x, a = map(int, input().split())
    X[t], A[t] = x ,a
    
dp=[[-10**18] * (M+1) for _ in range(5)]
dp[0][0]=0
 
for t in range(1, M+1):
    for i in range(5):
        dp[i][t] = dp[i][t-1]
        if i != 0:
            dp[i][t] = max(dp[i][t], dp[i-1][t-1])
        if i != 4:
            dp[i][t] = max(dp[i][t], dp[i+1][t-1])
    dp[X[t]][t] += A[t]
    
ans = 0
for i in range(5):
    ans = max(ans, dp[i][-1])
print(ans)