N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

C = A + B
C.sort()
d = dict()

for i in range(N+M):
    d[C[i]] = i+1

ans = []
for i in range(N):
    ans.append(d[A[i]])
print(*ans)
ans = []
for i in range(M):
    ans.append(d[B[i]])
print(*ans)