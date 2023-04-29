N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(M)]

dp = [[10**9] * (2 ** N) for _ in range(M+1)]
dp[0][0] = 0
for i in range(1, M+1):
    for j in range(2**N):
        nlist = [None] * N
        for k in range(N):
            if (j // (2 ** k)) % 2 == 0:
                nlist[k] = 0
            else:
                nlist[k] = 1
        
        v = 0
        for k in range(N):
            if nlist[k] == 1 or A[i-1][k] == 1:
                v += 2 ** k
        
        dp[i][j] = min(dp[i][j], dp[i-1][j])
        dp[i][v] = min(dp[i][v], dp[i-1][j] + 1)
#print(dp) 
if dp[M][-1] == 10**9:
    print(-1)
else:
    print(dp[M][-1])