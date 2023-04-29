N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]
S = input()

nlist = []
for i in range(N):
    nlist.append([xy[i][1], xy[i][0], S[i]])
nlist.sort()
nlist = sorted(nlist, key=lambda x: (x[0], x[1]))
for i in range(N-1):
    if nlist[i][0] == nlist[i+1][0]:
        if nlist[i][2] != nlist[i+1][2] and nlist[i][2] == "R":
            print("Yes")
            exit()
print("No")