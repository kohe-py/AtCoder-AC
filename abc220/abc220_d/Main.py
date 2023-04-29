from collections import deque
N = int(input())
A = list(map(int, input().split()))

mod = 998244353
d = deque(A)
dp = [[0] * (10) for _ in range(N-1)]
dp[0][A[0]*A[1]%10] += 1
dp[0][(A[0] + A[1])%10] += 1 

for i in range(1, N):
    for j in range(10):
        if i+1 <= N-1:
            dp[i][(j*A[i+1])%10] += (dp[i-1][j]%mod)
            dp[i][(j+A[i+1])%10] += (dp[i-1][j]%mod)

for i in range(len(dp[-1])):
    print(dp[-1][i] % mod)