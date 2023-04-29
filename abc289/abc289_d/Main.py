N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = set(map(int, input().split()))
X = int(input())

dp = [False] * (X+1)
dp[0] = True
for i in range(X+1):
    for j in range(N):
        if dp[i] and i+A[j] not in B:
            if i + A[j] <= X:
                dp[i+A[j]] = True
if dp[-1]:
    print("Yes")
else:
    print("No")