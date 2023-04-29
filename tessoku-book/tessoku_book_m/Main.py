N,K=map(int, input().split())
A=list(map(int,input().split()))
ans=0
j=0
for i in range(N):
    j = max(j, i + 1)
    while j < N and A[j] - A[i] <= K:
        j += 1
    ans += (j - i - 1)
print(ans)