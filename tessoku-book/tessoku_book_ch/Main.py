N = int(input())

nlist = [[0] * (1503) for _ in range(1503)]

for i in range(N):
    a,b,c,d = map(int, input().split())
    nlist[a+1][b+1] += 1
    nlist[a+1][d+1] -= 1
    nlist[c+1][b+1] -= 1
    nlist[c+1][d+1] += 1
    
ruiseki = [[0] * (1503) for _ in range(1503)]

for i in range(1,1502):
    for j in range(1,1502):
        ruiseki[i][j] = ruiseki[i][j-1] + nlist[i][j]
for j in range(1,1502):
    for i in range(1,1502):
        ruiseki[i][j] = ruiseki[i-1][j] + ruiseki[i][j]

count = 0
for i in range(1,1502):
    for j in range(1,1502):
        if ruiseki[i][j]>=1:
            count += 1


print(count)