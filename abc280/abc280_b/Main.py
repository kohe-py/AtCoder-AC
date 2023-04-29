N = int(input())
S = list(map(int, input().split()))

A = [S[0]]
s = S[0]
for i in range(1,N):
    A.append(S[i] - s)
    s += A[i]
print(*A)   