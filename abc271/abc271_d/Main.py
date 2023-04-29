N, S = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * (S + 1) for _ in range(N + 1)]
dp[0][0] = 1

for i in range(1, N + 1):
    for j in range(S + 1):
        if dp[i - 1][j] != 0 and j + ab[i - 1][0] <= S:
            dp[i][ab[i - 1][0] + j] += dp[i - 1][j]
        if dp[i - 1][j] != 0 and j + ab[i - 1][1] <= S:
            dp[i][ab[i - 1][1] + j] += dp[i - 1][j]

if dp[-1][S] >= 1:
    print("Yes")
else:
    print("No")
    exit()

now = S
ans = ""
for i in reversed(range(1, N + 1)):
    if 0 <= now - ab[i - 1][0] <= S and dp[i - 1][now - ab[i - 1][0]] > 0:
        now -= ab[i - 1][0]
        ans = "H" + ans
    else:
        now -= ab[i - 1][1]
        ans = "T" + ans
print(ans)