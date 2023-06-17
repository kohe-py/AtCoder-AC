X, Y, Z = map(int, input().split())
S = input()

leng = len(S)
dp = [[10 ** 18, 10 ** 18] for _ in range(leng + 1)] ## [on, off]
dp[0][1] = 0
for i in range(1, leng + 1):
    if S[i - 1] == "a":
        dp[i][0] = min(dp[i - 1][0] + Y, dp[i - 1][1] + Z + Y)
        dp[i][1] = min(dp[i - 1][0] + Z + X, dp[i - 1][1] + X)
    else:
        dp[i][0] = min(dp[i - 1][0] + X, dp[i - 1][1] + Z + X)
        dp[i][1] = min(dp[i - 1][0] + Z + Y, dp[i - 1][1] + Y)

#print(dp)
print(min(dp[-1]))