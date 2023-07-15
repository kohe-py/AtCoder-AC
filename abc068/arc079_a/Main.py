N, M = map(int, input().split())
g = [[] for i in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)

from collections import deque
todo = deque()
todo.append(0)
dist = [-1] * N
dist[0] = 0

while todo:
    v = todo.popleft()
    if dist[v] >= 2:
        break
    for nx in g[v]:
        if dist[nx] == -1:
            dist[nx] = dist[v] + 1
            todo.append(nx)

if dist[-1] != -1 and dist[-1] <= 2:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")