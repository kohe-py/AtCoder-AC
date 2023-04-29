N, M = map(int, input().split())
kx = [list(map(int, input().split())) for _ in range(M)]

nlist = [[0] * N for _ in range(N)]
for i in range(M):
    for j in range(kx[i][0]):
        for k in range(kx[i][0]):
            nlist[kx[i][k+1] - 1][kx[i][j+1] - 1] = 1
            nlist[kx[i][j+1] - 1][kx[i][k+1] - 1] = 1

#print(nlist)
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        else:
            if nlist[i][j] == 1:
                pass
            else:
                print("No")
                exit()
print("Yes")