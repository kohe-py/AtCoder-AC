N, X = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(N)]

a = []
for i in range(N):
    for j in range(ab[i][1]):
        a.append(ab[i][0])

dp = [[-1] * (X+1) for _ in range(len(a)+1)]
dp[0][0] = 0
for i in range(1, len(a)+1):
    for j in range(X+1):
        if dp[i-1][j] != -1:
            dp[i][j] = dp[i-1][j]
            if dp[i][j] == X:
                print("Yes")
                exit()
        if j - a[i-1] >= 0 and dp[i-1][j - a[i-1]] != -1:
            dp[i][j] = dp[i-1][j-a[i-1]]+a[i-1]
            if dp[i][j] == X:
                print("Yes")
                exit()
            
print("No")