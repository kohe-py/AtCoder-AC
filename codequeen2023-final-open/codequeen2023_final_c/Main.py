from sys import setrecursionlimit
setrecursionlimit(10 ** 8)

N, S, T = map(int, input().split())
g = [[] for _ in range(N)]

for _ in range(N - 1):
    u, v = map(int, input().split())
    g[u - 1].append(v - 1)
    g[v - 1].append(u - 1)

prev = [-1] * N
def DFS(n, p):
    for nv in g[n]:
        if nv == p:
            continue
        prev[nv] = n
        DFS(nv, n)
  
DFS(S - 1, -1)
now = T - 1
path = {T - 1}
while prev[now] != -1:
    now = prev[now]
    path.add(now)


from collections import deque
ans = [-1 for _ in range(N)]
ans[S - 1] = 1
for i in path:
    ans[i] = 1
visit = {S - 1}

todo = deque([S - 1])
while todo:
    v = todo.popleft()
    for nx in g[v]:
        if nx not in visit:
            if nx not in path:
                ans[nx] = ans[v] + 1
            todo.append(nx)
            visit.add(nx)

for i in range(N):
    if i == S - 1 or i == T - 1 or i in path:
        print(1)
    else:
        print(ans[i])