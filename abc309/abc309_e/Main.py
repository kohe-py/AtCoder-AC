N, M = map(int, input().split())

g = [[] * N for _ in range(N)]
p = list(map(int, input().split()))
for i in range(N - 1):
    g[p[i] - 1].append(i + 1)

from collections import deque, defaultdict

def bfs(todo):
   while todo:
        v = todo.popleft()
        for nx in g[v]:
            dist[nx] = max(dist[nx], dist[v] - 1)
            todo.append(nx)


dist = [-1] * N
for _ in range(M):
    x, y = map(int, input().split())
    x -= 1
    dist[x] = max(dist[x], y)

bfs(deque([0]))
ans = 0
for i in range(N):
    if dist[i] >= 0:
        ans += 1
print(ans)