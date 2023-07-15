N, M, K = map(int, input().split())
g = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)
from collections import deque
dist = [-1] * N
s = []
for _ in range(K):
    p, h = map(int, input().split())
    p -= 1
    s.append((p, h))
    dist[p] = max(dist[p], h)


s.sort(reverse=True, key=lambda x: x[1])
for i, j in s:
    todo = deque([i])
    while todo:
        v = todo.popleft()
        for nx in g[v]:
            if dist[nx] < dist[v] - 1:
                dist[nx] = dist[v] - 1
                todo.append(nx)
ans = 0
li = []
for i in range(N):
    if dist[i] >= 0:
        ans += 1
        li.append(i + 1)

print(ans)
print(*li)