N, D = map(int, input().split())
xy = [list(map(int, input().split())) for _ in range(N)]

g = [[] for _ in range(N)]
#print("-----------")
for i in range(N):
    for j in range(N):
        if i != j:
            x1, y1 = xy[i][0], xy[i][1]
            x2, y2 = xy[j][0], xy[j][1]
            #print(x1, x2, y1, y2)
            dist = (x1 - x2) ** 2 + (y1 - y2) ** 2
            #print(dist, x1 - x2, y1 - y2)
            if dist <= D ** 2:
                #print(i, j)
                g[i].append(j)
 
#print("-----------------")
#print(g)
seen = [False] * N
from collections import deque
todo = deque()
todo.append(0)
seen[0] = True

while todo:
    v = todo.popleft()
    #print(v)
    for nx in g[v]:
        if seen[nx] == False:
            #print(nx)
            seen[nx] = True
            todo.append(nx)

for i in range(N):
    if seen[i]:
        print("Yes")
    else:
        print("No")