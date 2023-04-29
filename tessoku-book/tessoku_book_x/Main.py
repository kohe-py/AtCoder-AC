import bisect

N = int(input())
A = list(map(int, input().split()))

dp = [5000000] * N
L = [5000000] * N
dp[0] = 1
L[0] = A[0]

for i in range(1, N):
    x = bisect.bisect_right(L, A[i])
    if x <= 0:
        dp[i] = 1
        L[0] = min(L[0], A[i])
    else:
        if L[x-1] == A[i]:
            dp[i] = dp[x-1]
        else:
            dp[i] = x
            L[x] = min(L[x], A[i])

#print(dp)
#print(L)
for i in range(N):
    if L[i] == 5000000:
        ans = i
        break
    ans = N
print(ans)