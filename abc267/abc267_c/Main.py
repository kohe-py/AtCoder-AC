from collections import deque
N, M = map(int, input().split())
A = deque(map(int, input().split()))
#print(A)
result = 0
B = [0] * (N+1)
for i in range(N):
    B[i+1] = A[i] + B[i]
    if i < M:
        result += (i+1)*A[i]
#print(B)
ans = result
#print(ans)
for i in range(N-M):
    result -= A[i]
    result += (A[i+M]*M)
    result -= (B[i+M] - B[i+1])
    ans = max(ans, result)
print(ans)