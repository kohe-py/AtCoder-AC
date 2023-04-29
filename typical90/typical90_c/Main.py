N = int(input())
g = [[] for _ in range(N)]
for _ in range(N - 1):
    A, B = map(int, input().split())
    g[A - 1].append(B - 1)
    g[B - 1].append(A - 1)

from collections import deque

dist = [-1] * N
dist[0] = 0
todo = deque([0])

while todo:
    v = todo.popleft()
    for nx in g[v]:
        if dist[nx] == -1:
            todo.append(nx)
            dist[nx] = dist[v] + 1
            max_v = nx

#print(dist)

dist = [-1] * N
dist[max_v] = 0
todo = deque([max_v])
result = 0

while todo:
    v = todo.popleft()
    for nx in g[v]:
        if dist[nx] == -1:
            todo.append(nx)
            dist[nx] = dist[v] + 1
            result = max(result, dist[v] + 1)
            max_v = nx


print(result + 1)