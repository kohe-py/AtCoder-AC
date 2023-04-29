N, S = map(int, input().split())
A = list(map(int, input().split()))

dp = [[0] * (S+1) for _ in range(N+1)]
dp[0][0] = True
for i in range(1,N+1):
    for j in range(S+1):
        #print(j, j-A[i-1])
        if dp[i-1][j]:
            dp[i][j] = True
        if j - A[i-1] >= 0:
            if dp[i-1][j-A[i-1]]:
                dp[i][j] = True
        else:
            pass
if dp[-1][-1] == False:
    print(-1)
    exit()
ans = [N]
for i in range(N, 1, -1):
    if S == 0:
        break
    
    if dp[i-1][S]:
        ans.pop()
        ans.append(i-1)
        
    elif S - A[i-1] > 0 and dp[i-1][S-A[i-1]] == True:
        ans.append(i-1)
        S -= A[i-1]

    else:
        pass
ans.sort()
print(len(ans))
print(*ans) 