H, W, N = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1] * W for _ in range(H)]
for i in range(N):
    ab[i][0] -= 1
    ab[i][1] -= 1
    dp[ab[i][0]][ab[i][1]] = 0
# dp[i][j] 座標i, jを右下とする一番おっきい正方形の一辺
for i in range(H):
    for j in range(W):
        if dp[i][j] != -1:
            continue
        if i - 1 >= 0 and j - 1 >= 0:
            dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
        else:
            dp[i][j] = 1

ans = 0
for i in range(H):
    for j in range(W):
        ans += max(0, dp[i][j])

print(ans)