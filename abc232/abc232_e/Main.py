H, W, K = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())

mod = 998244353
# 列が同じ　行が同じ　列行ともに同じ　どっちも違う
dp = [[0] * 4 for i in range(K + 1)]
if x1 == x2 and y1 == y2:
    dp[0][2] = 1
elif x1 == x2:
    dp[0][1] = 1
elif y1 == y2:
    dp[0][0] = 1
else:
    dp[0][3] = 1

for i in range(1, K + 1):
    dp[i][2] = (dp[i - 1][0] + dp[i - 1][1])
    dp[i][1] = (dp[i - 1][3] + dp[i - 1][2] * (W - 1) + dp[i - 1][1] * (W - 2))
    dp[i][0] = (dp[i - 1][3] + dp[i - 1][2] * (H - 1) + dp[i - 1][0] * (H - 2))
    dp[i][3] = (dp[i - 1][0] * (W - 1) + dp[i - 1][1] * (H - 1) + dp[i - 1][3] * (H - 2 + W - 2))
    for j in range(4):
        dp[i][j] %= mod

#print(dp)
print(dp[-1][2])