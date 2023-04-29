N, W = map(int, input().split())
wv = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * (W+1) for _ in range(N+1)]
dp[0][W] = 0
for i in range(N):
    for w in range(W+1):
        if wv[i][0] > w:
            dp[i+1][w] = dp[i][w]
        else:
            dp[i+1][w] = max(dp[i][w], dp[i][w - wv[i][0]]+wv[i][1])
        
#print(dp)
print(dp[N][W])