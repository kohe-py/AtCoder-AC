N, K = map(int, input().split())
h = list(map(int, input().split()))


dp = [10**5 for _ in range(N)] 
    
dp[0] = 0
dp[1] = abs(h[1] - h[0])

for i in range(2, N):
    dp[i] = dp[i-1] + abs(h[i] - h[i-1])
    for k in range(2, K + 1):
        if k <= i:
            dp[i] = min(abs(h[i] - h[i-k]) + dp[i-k], dp[i])

print(dp[N-1])