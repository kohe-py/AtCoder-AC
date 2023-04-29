N, Q = map(int, input().split())
A = list(map(int, input().split()))

B = [A[0]]
for i in range(1,N):
    B.append(B[i-1]+A[i])

for i in range(Q):
    L, R = map(int, input().split())
    if L == 1:
        print(B[R-1])
    else:
        print(B[R-1] - B[L-2])