D = int(input())
N = int(input())

B = [0] * (D+1)
for i in range(N):
    L,R = map(int, input().split())
    B[L-1] += 1
    B[R] -= 1

A = [B[0]]
for j in range(1,D+1):
    A.append(A[j-1] + B[j])
for k in range(D):
    print(A[k])
