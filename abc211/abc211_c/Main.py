from collections import deque, defaultdict, Counter

# chokudai
S = input()
N = len(S)
T = "chokudai"

dp = [[0] * (9) for _ in range(N+1)]
dp[0][0] = 1
for i in range(1, N+1):
    for j in range(9):
        dp[i][j] += dp[i-1][j] % 1000000007
        if j != 0 and S[i-1] == T[j-1]:
            dp[i][j] += dp[i-1][j-1] % 1000000007
        
            
print(dp[-1][-1] % 1000000007)
#print(dp)