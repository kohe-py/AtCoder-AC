def chmax(dp, i, j, k):
    if dp[i][j] < k:
        dp[i][j] = k
        return True
    return False

S = str(input())
T = str(input())

dp = [[0 for j in range(len(T)+1)]for i in range(len(S)+1)]
dp0 = 0
dp[0][0] = 0

for i in range(len(S)):
    for j in range(len(T)):
        if S[i] == T[j]:
            chmax(dp,i+1,j+1, dp[i][j] + 1)
        else:
            chmax(dp,i+1,j+1, dp[i+1][j])
            chmax(dp,i+1,j+1, dp[i][j+1])
            
ans = ""
i = len(S)
j = len(T)
while (i>0  and j>0):
    if dp[i][j] == dp[i-1][j]:
        i -= 1
    elif dp[i][j] == dp[i][j-1]:
        j -= 1
    else:
        ans += S[i-1] 
        i -= 1
        j -= 1
    
print(ans[::-1])