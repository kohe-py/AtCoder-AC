N = int(input())
abc = [list(map(int, input().split())) for _ in range(N)]

dp = [[0, 0, 0] for _ in range(N+1)]

dp[1][0] = abc[0][0]
dp[1][1] = abc[0][1]
dp[1][2] = abc[0][2]

for i in range(2,N+1):
    for k in range(3):
        dp[i][0] = abc[i-1][0] + max(dp[i-1][1], dp[i-1][2])
        dp[i][1] = abc[i-1][1] + max(dp[i-1][2], dp[i-1][0])
        dp[i][2] = abc[i-1][2] + max(dp[i-1][0], dp[i-1][1])
        

print(max(dp[N]))