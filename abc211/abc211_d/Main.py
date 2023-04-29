from collections import deque
N, M = map(int, input().split())
g = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)


todo = []
todo.append(0)
dist = [None] * N
count = [0] * N
count[0] = 1
dist[0] = 0

for v in todo:
    for nv in g[v]:
        if dist[nv] is None:
            dist[nv] = dist[v] + 1
            todo.append(nv)
            count[nv] = count[v]
        elif dist[nv] == dist[v] + 1:
            count[nv] += count[v]
            count[nv] %= 1000000007
print(count[N-1])