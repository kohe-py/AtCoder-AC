N = int(input())
S = input()

mod = 10**9 + 7
s = "atcoder"
leng = len(s)
dp = [[-1] * (leng + 1) for _ in range(N + 1)]
for i in range(N + 1):
    dp[i][0] = 1

for i in range(1, N + 1):
    for j in range(1, leng + 1):
        dp[i][j] = dp[i-1][j]
        if S[i - 1] == s[j - 1]:
            if dp[i - 1][j - 1] != -1:
                if dp[i][j] == -1:
                    dp[i][j] = dp[i-1][j - 1]

                else:
                    dp[i][j] += dp[i - 1][j - 1]
                    dp[i][j] %= mod

if dp[-1][-1] == -1:
    print(0)
    exit()
print(dp[-1][-1] % mod)
