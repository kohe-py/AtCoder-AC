N = int(input())

dp = [[0] * 11 for _ in range(N)]
#遷移: １桁目→２桁目 ... 
#      dp[i][j] i桁の先頭がjのやつの個数
#      dp[i][j] = dp[i-1][j] + dp[i-1][j-1] + dp[i-1][j+1]

#初期
for i in range(1, 10):
    dp[0][i] = 1

for i in range(1, N):
    for j in range(1, 10):
        dp[i][j] = (dp[i-1][j] + dp[i-1][j-1] + dp[i-1][j+1]) % 998244353
ans = 0
for i in range(11):
    ans += dp[-1][i]
print(ans % 998244353)