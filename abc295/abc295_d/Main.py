from collections import defaultdict
S = input()
N = len(S)

dp = [[2]*10 for _ in range(N+1)]
for i in range(1, N+1):
    x = int(S[i-1])
    for j in range(10):
        dp[i][j] = dp[i-1][j]
    if dp[i][x] == 2:
        dp[i][x] -= 1
    else:
        dp[i][x] += 1

d = defaultdict(int)
count = 0
for i in range(1, N+1):
    #print(dp[i])
    dp[i] = "".join(map(str, dp[i]))
    d[dp[i]] += 1
    if dp[i].count("1") == 0:
        count += 1

ans = count
for i in d:
    ans += d[i] * (d[i] - 1) // 2
print(ans)