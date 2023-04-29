H,W = map(int, input().split())
c = [input() for _ in range(H)]

dp = [[0] * (W) for _ in range(H)]
for i in range(W):
    if c[0][i] == "#":
        break
    else:
        dp[0][i] = 1
for i in range(H):
    if c[i][0] == "#":
        break
    else:
        dp[i][0] = 1
        
for i in range(1, H):
    for j in range(1, W):
        if c[i][j] == "#":
            dp[i][j] = 0
        else:
            #dp[i][j] = 0
            if c[i-1][j] == ".":
                dp[i][j] += dp[i-1][j]
            if c[i][j-1] == ".":
                dp[i][j] += dp[i][j-1]
#print(dp)
print(dp[-1][-1])