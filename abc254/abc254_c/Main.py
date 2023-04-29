N, K = map(int, input().split())
A = list(map(int, input().split()))

if K == 1:
    print("Yes")
    exit()
    
B = [[] for _ in range(K)]
for i in range(N):
    B[i % K].append(A[i])

for i in range(K):
    B[i].sort()

sort_a = [None] * N
for i in range(N):
    sort_a[i] = B[i % K][i // K]

print("Yes" if sort_a == sorted(A) else "No")