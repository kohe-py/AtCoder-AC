N, K = map(int, input().split())
a = list(map(int, input().split()))

dp = [0] * (K + 1)
dp[0] = 0

for i in range(K + 1):
    for j in range(N):
        if dp[i] == 0 and i + a[j] <= K:
            dp[i + a[j]] = 1


if dp[K] == 1:
    print("First")
else:
    print("Second")