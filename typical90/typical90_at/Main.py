N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

for i in range(N):
    A[i] %= 46
    B[i] %= 46
    C[i] %= 46

dp = [[0] * (46 * 3 + 1) for _ in range(3)]
for i in range(N):
    dp[0][A[i]] += 1

for i in range(1, 3):
    for j in range(N):
        for k in range(46*3+1):
            if i == 1 and k - B[j] >= 0 and dp[i-1][k - B[j]] > 0:
                dp[i][k] += dp[i-1][k - B[j]]
            if i == 2 and k - C[j] >= 0 and dp[i-1][k - C[j]] > 0:
                dp[i][k] += dp[i-1][k - C[j]]

ans = 0
ans += (dp[2][0] + dp[2][46] + dp[2][46*2] + dp[2][46*3])
print(ans)


