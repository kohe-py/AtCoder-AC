N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * 2 for _ in range(N)]

for i in range(N):
    if i == 0:
        dp[i][0] = 1
        dp[i][1] = 1
    else:
        for j in range(2):
            for k in range(2):
                if xy[i-1][j] != xy[i][k]:
                    dp[i][k] += dp[i-1][j]
    dp[i][0] %= 998244353
    dp[i][1] %= 998244353

print((dp[-1][0] + dp[-1][1])%998244353)