N, W = map(int, input().split())
wv = [list(map(int, input().split())) for _ in range(N)]

V = 0
for i in range(N):
    V += wv[i][1]
    
dp = [[0] * (V+1) for _ in range(N+1)]
    
for v in range(1, V+1):
    dp[0][v] = W+1

for i in range(N):
    for v in range(V+1):
        if wv[i][1] <= v:
            dp[i+1][v] = min(dp[i][v],dp[i][v - wv[i][1]] + wv[i][0])
        else:
            dp[i+1][v] = dp[i][v]

ans = 0
for v in range(V+1):
    if dp[-1][v] <= W:
        ans = max(ans, v)

print(ans)