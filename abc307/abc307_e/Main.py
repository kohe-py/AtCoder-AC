N, M = map(int, input().split())

mod = 998244353
dp = [[0] * (2)  for i in range(N)]
dp[0][0] = M
for i in range(1, N):
    dp[i][1] += (dp[i - 1][0] * (M - 1))
    dp[i][1] += (dp[i - 1][1] * (M - 2))
    dp[i][0] += dp[i - 1][1]
    dp[i][1] %= mod
    dp[i][0] %= mod

ans = 0
ans += dp[-1][-1]
print(ans)