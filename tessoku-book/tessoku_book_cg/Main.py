N = int(input())
nlist = [[0] * 1501 for _ in range(1501)]

for i in range(N):
    x, y = map(int, input().split())
    nlist[y][x] += 1

ruiseki = [[0] * 1501 for _ in range(1501)]
for i in range(1,1501):
    for j in range(1501):
        ruiseki[i][j] = ruiseki[i-1][j] + nlist[i][j]

for j in range(1, 1501):
    for i in range(1501):
        ruiseki[i][j] = ruiseki[i][j-1] + ruiseki[i][j]
#print(ruiseki)
Q = int(input())
for i in range(Q):
    a,b,c,d = map(int, input().split())
    print(ruiseki[d][c] + ruiseki[b-1][a-1] - ruiseki[d][a-1] -ruiseki[b-1][c])