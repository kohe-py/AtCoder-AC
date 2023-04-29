N = int(input())
B = [[0] * (1002) for _ in range(1002)]
for i in range(N):
    x, y, z, w = map(int, input().split())
    B[x][y] += 1
    B[x][w] -= 1
    B[z][w] += 1
    B[z][y] -= 1

for i in range(1002):
    for j in range(1001):
        B[i][j + 1] += B[i][j]

for i in range(1001):
    for j in range(1002):
        B[i + 1][j] += B[i][j]

ans = [0] * N
for i in range(1002):
    for j in range(1002):
        if B[i][j] != 0:
            #print(B[i][j])
            ans[B[i][j] - 1] += 1

for i in range(N):
    print(ans[i])

