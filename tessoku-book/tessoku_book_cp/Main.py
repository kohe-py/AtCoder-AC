N = int(input())
h = list(map(int, input().split()))

dp = [0]*(N+1)
dp[2] = abs(h[0] - h[1])
dp2 = [0]*(N+1)
dp2[2] = 1
for i in range(3, N+1):
    if dp[i-1]+abs(h[i-1] - h[i-2]) > dp[i-2]+abs(h[i-1] - h[i-3]):
        dp[i] = dp[i-2]+abs(h[i-1] - h[i-3])
        dp2[i] = 2
    else:
        dp[i] = dp[i-1]+abs(h[i-1] - h[i-2])
        dp2[i] = 1

        
ans=[N]
while True:
    ans.append(N - dp2[N])
    N -= dp2[N]
    #print(N)
    if N == 1:
        break
ans.sort()
print(len(ans))
print(*ans)