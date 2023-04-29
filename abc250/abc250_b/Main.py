N, A, B = map(int, input().split())

nlist = [[0] * (N) for _ in range(N)]
flag = True
for i in range(N):
    if i % 2 == 0:
        flag = True
    else:
        flag = False 
    for j in range(N):
        if flag:
            if j % 2 == 0:
                nlist[i][j] = "."
            else:
                nlist[i][j] = "#"
        else:
            if j % 2 == 1:
                nlist[i][j] = "."
            else:
                nlist[i][j] = "#"
#print(*nlist)
ans = [0] * N
for i in range(N):
    ans[i] = []
    for j in range(N):
        for k in range(B):
            ans[i].append(nlist[i][j])

result = []
for i in range(N):
    for k in range(A):
        result.append(ans[i])

for i in range(N*A):
    print("".join(result[i]))