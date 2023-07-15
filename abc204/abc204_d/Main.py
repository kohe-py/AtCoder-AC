N = int(input())
T = list(map(int, input().split()))

T.sort(reverse=True)
result = sum(T)

dp = [[-1] * (result + 1) for _ in range(N + 1)]
for i in range(N):
    dp[i][0] = 1

for i in range(1, N + 1):
    for j in range(result + 1):
        if dp[i - 1][j] != -1:
            dp[i][j + T[i - 1]] = 1
            dp[i][j] = 1

ans = 10 ** 18
for j in range(result + 1):
    if dp[-1][j] != -1: 
        ans = min(ans, max(j, result - j))
#print(result)
print(ans)