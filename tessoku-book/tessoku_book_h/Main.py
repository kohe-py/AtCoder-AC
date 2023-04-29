H,W = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(H)]
Q = int(input())

F = [[0] * (W) for _ in range(H)]
for i in range(H):
    F[i][0] = X[i][0]
    for j in range(1,W):
        F[i][j] = F[i][j-1] + X[i][j]

for j in range(W):
    for i in range(1,H):
        F[i][j] = F[i-1][j] + F[i][j]

#print(F)
for i in range(Q):
    A,B,C,D = map(int, input().split())
    A -= 1
    B -= 1
    C -= 1
    D -= 1
    if A == 0 and B != 0:
        print(F[C][D] - F[C][B-1])
    elif A != 0 and B == 0:
        print(F[C][D] - F[A-1][D])
    elif A == 0 and B == 0:
        print(F[C][D])
    else:
        print(F[C][D] - F[A-1][D] - F[C][B-1] + F[A-1][B-1])