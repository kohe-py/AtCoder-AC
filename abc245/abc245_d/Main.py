N, M = map(int, input().split())
A = list(map(int, input().split()))
C = list(map(int, input().split()))

B = [0] * (M+1)
for i in reversed(range(M+1)):
    B[i] = C[N+i] // A[N]
    for j in range(N+1):
        C[j+i] -= (B[i] * A[j])

print(*B)
