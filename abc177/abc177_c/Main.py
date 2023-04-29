N = int(input())
A = list(map(int, input().split()))

B = [0] * (N+1)
for i in range(N):
    B[i+1] = B[i] + A[i] 
#print(B)
ans = 0
for i in range(N):
    X = A[i] * (B[N] - B[i+1])
    #print(X)
    ans += X
print(ans%1000000007)