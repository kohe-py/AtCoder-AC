H,W,N = map(int, input().split())
nlist = [[0]*(W+2) for i in range(H+2)]

for i in range(N):
    a,b,c,d = map(int, input().split())
    nlist[a][b] += 1
    nlist[c+1][b] -= 1
    nlist[a][d+1] -= 1
    nlist[c+1][d+1] += 1
#print(nlist)

ruiseki =  [[0]*(W+2) for i in range(H+2)]

for i in range(1,H+1):
    for j in range(1,W+1):
        ruiseki[i][j] = ruiseki[i][j-1] + nlist[i][j]

for j in range(1, W+1):
    for i in range(1, H+1):
        ruiseki[i][j] = ruiseki[i-1][j] + ruiseki[i][j]

for i in range(1,H+1):
    ruiseki[i] = ruiseki[i][1:W+1]
    print(*ruiseki[i])