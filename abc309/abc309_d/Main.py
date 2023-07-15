N, N1, M = map(int, input().split())
g = [[] * (N + N1) for i in range(N + N1)]
for i in range(M):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)

from collections import deque
todo = deque([0])
dist = [-1] * (N + N1)
dist[0] = 0

while todo:
    v = todo.popleft()
    for nx in g[v]:
        if dist[nx] == -1:
            dist[nx] = dist[v] + 1
            todo.append(nx)

todo1 = deque([N + N1 - 1])
dist1 = [-1] * (N + N1)
dist1[N + N1 - 1] = 0
while todo1:
    v = todo1.popleft()
    for nx in g[v]:
        if dist1[nx] == -1:
            dist1[nx] = dist1[v] + 1
            todo1.append(nx)

print(max(dist) + max(dist1) + 1)