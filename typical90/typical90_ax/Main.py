N, L = map(int, input().split())

mod = 10**9 + 7
dp = [[0, 0] for _ in range(N+1)]
dp[0] = [0, 1]
# 0 L段　　1 1段

for i in range(N+1):
    if i + L <= N:
        dp[i + L][0] = (sum(dp[i]) % mod)
    if i + 1 <= N:
        dp[i + 1][1] = (sum(dp[i]) % mod)

print(sum(dp[-1]) % mod)