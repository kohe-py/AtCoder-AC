N, K = map(int, input().split())
A = list(map(int, input().split()))

B = [0] * (N+1)
for i in range(N):
    B[i+1] = A[i] + B[i]

ans = 0
#print(len(B))

for i in range(1,N+1):
    j = 0
    j = max(j, i)
    while j <= N and B[j] - B[i-1] <= K:
        #print(B[j] - B[i])
        j += 1
        ans += 1

print(ans)