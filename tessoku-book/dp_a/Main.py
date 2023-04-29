N = int(input())
h = list(map(int, input().split()))

dp = [0]*(N+1)
dp[2] = abs(h[0] - h[1])
for i in range(3, N+1):
    dp[i] = min(dp[i-1]+abs(h[i-1] - h[i-2]), dp[i-2]+abs(h[i-1] - h[i-3]))
print(dp[N])