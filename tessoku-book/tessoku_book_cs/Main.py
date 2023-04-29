S = input()
T = input()

dp = [[10**7] * (len(T)+1) for _ in range(len(S) + 1)]
for i in range(len(S)+1):
    dp[i][0] = i
for j in range(1, len(T)+1):
    dp[0][j] = j

#print(dp)
for i in range(1, len(S) + 1):
    for j in range(1,len(T) + 1):
        if S[i-1] == T[j-1]:
            dp[i][j] = min(dp[i-1][j-1], dp[i][j-1] + 1, dp[i-1][j] + 1)
        if S[i-1] != T[j-1]:
            dp[i][j] = min(dp[i-1][j-1] + 1, dp[i][j-1] + 1, dp[i-1][j] + 1)
        
#print(dp)
print(dp[-1][-1])