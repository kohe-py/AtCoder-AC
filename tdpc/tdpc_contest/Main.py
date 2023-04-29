N = int(input())
p =list(map(int, input().split()))

M = 100

dp =[[0 for j in range(N*M +1)]for i in range(N+1)]
dp[0][0] = 1
for i in range(1,N+1):
    for j in range(M*N +1):
        if j >= p[i-1]:
            if dp[i-1][j]==1 or dp[i-1][j - p[i-1]]==1:
                dp[i][j] = 1
        else:
            if dp[i-1][j]==1:
                dp[i][j] = 1
ans = 0
for j in range(N*M +1):
    if dp[N][j] == 1:
        ans += 1
print(ans)
    