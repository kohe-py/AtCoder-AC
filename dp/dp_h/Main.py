H, W = map(int, input().split())
a = [list(input()) for _ in range(H)]

mod = 10 ** 9 + 7
dp = [[0] * W for _ in range(H)]
dp[0][0] = 1

# 右 と 下 に進む
for i in range(H):
    for j in range(W):
        if j < W - 1 and dp[i][j] != 0 and a[i][j + 1] != "#":
            dp[i][j + 1] += dp[i][j]
            dp[i][j + 1] %= mod
        if i < H - 1 and dp[i][j] != 0 and a[i + 1][j] != "#":
            dp[i + 1][j] += dp[i][j]
            dp[i + 1][j] %= mod
print(dp[-1][-1])