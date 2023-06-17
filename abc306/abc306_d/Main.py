N = int(input())

dp = [[0] * 2 for _ in range(N + 1)]
dp[0] = [0, 0]

for i in range(1, N + 1):
    X, Y = map(int, input().split())
    #print(dp)
    if X == 0:
        dp[i][0] = max(dp[i - 1][0] + Y, dp[i - 1][1] + Y, dp[i - 1][0])
        dp[i][1] = dp[i - 1][1]
    else:
        dp[i][1] = max(dp[i - 1][0] + Y, dp[i - 1][1])
        dp[i][0] = dp[i - 1][0]

print(max(dp[-1]))