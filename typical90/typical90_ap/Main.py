K = int(input())

if K % 9 != 0:
    print(0)
    exit()

mod = 10 ** 9 + 7

## K は　10^5　
## 9*11111 < 10^5

dp = [0] * (K + 1)
dp[0] = 1
for i in range(1, K + 1):
    for j in range(1, 10):
        if i - j >= 0:
            dp[i] += dp[i - j]
            dp[i] %= mod

print(dp[-1] % mod)