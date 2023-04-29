N, M, K = map(int, input().split())

# 1 ≤ N,M ≤ 50 数列の要素の最大値M　
# N ≤ K ≤ NM　NMは数列の合計の最大値

dp = [[0] * (K+1) for _ in range(N)]
# dp[i][j] は i番目までの和jの個数
for i in range(1, M+1):
    dp[0][i] = 1
    
for i in range(1, N):
    for j in range(1, K+1):
        for k in range(1, M+1):
            if j + k <= K:
                dp[i][j+k] += dp[i-1][j]
#print(dp)
ans = 0
for i in range(N, K+1):
    ans += (dp[-1][i] % 998244353)
print(ans % 998244353)