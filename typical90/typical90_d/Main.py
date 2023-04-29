H, W = map(int, input().split())
A = [list(map(int ,input().split())) for _ in range(H)]

x = []
y = []
for i in range(H):
    x.append(sum(A[i]))
for i in range(W):
    result = 0
    for j in range(H):
        result += A[j][i]
    y.append(result)

for i in range(H):
    p = [0] * W
    for j in range(W):
        p[j] -= A[i][j]
        p[j] += (x[i] + y[j])
    print(*p)