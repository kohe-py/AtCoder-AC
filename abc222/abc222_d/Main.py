N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# dp[i][j] := 数列のi番目にjを持つ答えの数
leng = max(max(A), max(B))
dp = [[0] * (leng + 1) for _ in range(N + 1)]
dp[0] = [1] * (leng + 1)

for i in range(1, N + 1):
    for j in range(A[i - 1], B[i - 1] + 1):
        dp[i][j] += dp[i - 1][j]
        dp[i][j] %= 998244353
    for j in range(1, leng + 1):
        dp[i][j] += dp[i][j - 1]
        dp[i][j] %= 998244353

print(dp[-1][-1] % 998244353)