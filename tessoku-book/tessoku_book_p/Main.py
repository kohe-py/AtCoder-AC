N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
dp = [0] * (N+2)
dp[2] = A[0]
for i in range(3, N+1):
    dp[i] = min(dp[i-2]+B[i-3], dp[i-1]+A[i-2])
print(dp[N])