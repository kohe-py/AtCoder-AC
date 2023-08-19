S = list(input())
leng = len(S)

# (, )の個数の差で考えられる組み合わせの数
dp = [[0] * (leng + 1) for _ in range(leng + 1)]
dp[0][0] = 1
mod = 998244353

for i in range(leng):
    for j in range(leng):
        if S[i] != ")":
            dp[i + 1][j + 1] += dp[i][j]
            dp[i + 1][j + 1] %= mod
        if j != 0 and S[i] != "(":
            dp[i + 1][j - 1] += dp[i][j]
            dp[i + 1][j - 1] %= mod

#for i in range(leng + 1):
    #print(dp[i])
print(dp[leng][0])