from collections import deque
N = int(input())
sx, sy, tx, ty = map(int, input().split())
xyr = [list(map(int, input().split())) for _ in range(N)]

path_bool = [[] for _ in range(N)]
for i in range(N):
    x, y, r = xyr[i][0], xyr[i][1], xyr[i][2]
    if ((x-sx)**2 + (y-sy)**2) == r ** 2:
        s = i
    if ((x-tx)**2 + (y-ty)**2) == r ** 2:
        t = i
    for j in range(N):
        if i == j:
            continue
        else:
            x1, y1, r1 = xyr[j][0], xyr[j][1], xyr[j][2]
            dis = ((x-x1)**2 + (y-y1)**2)
            if abs(r-r1)**2 <= dis <= (r+r1)**2:
                path_bool[i].append(j)
                path_bool[j].append(i)
if s == t:
    print("Yes")
    exit()

def search(G, N, s):
    count = 0
    #seen = [False] * N
    todo = deque()
    
    seen[s] = True
    todo.append(s)
    
    while len(todo) != 0:
        v = todo.popleft()
        for n in G[v]:
            if seen[n]:
                continue
            else:
                seen[n] = True
                todo.append(n)

seen = [False] * N
search(path_bool, N, s)
if seen[t]:
    print("Yes")
else:
    print("No")