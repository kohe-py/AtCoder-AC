N, K = map(int, input().split())
A = list(map(int, input().split()))

dp = [0] * (N + 1)
for i in range(N + 1):
    for j in range(K):
        if A[j] > i:
            break
        dp[i] = max(dp[i], i - dp[i - A[j]])
print(dp[-1])
