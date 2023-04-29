N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [0] * (N+2)
dp[2] = A[0]
dp2 = [0] * (N+2)
dp2[2] = 1
for i in range(3, N+1):
    if dp[i-2]+B[i-3]< dp[i-1]+A[i-2]:
        dp[i] = dp[i-2]+B[i-3]
        dp2[i] = 2
    else:
        dp[i] = dp[i-1]+A[i-2]
        dp2[i] = 1


#print(dp) 
#print(dp2)
ans=[N]
while True:
    ans.append(N - dp2[N])
    N -= dp2[N]
    if N == 1:
        break
ans.sort()
print(len(ans))
print(*ans)