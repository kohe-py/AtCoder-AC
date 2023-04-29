N, X = map(int, input().split())
la = [list(map(int, input().split())) for _ in range(N)]

dp = [[] for _ in range(N+1)]
dp[0].append(1)
for i in range(1, N+1):
    for j in range(len(dp[i-1])):
        for k in range(la[i-1][0]):
            dp[i].append(dp[i-1][j] * la[i-1][k+1])
ans = 0
for i in range(len(dp[-1])):
    if dp[-1][i] == X:
        ans += 1
print(ans)