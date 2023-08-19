N, M = map(int, input().split())
g = [[] for _ in range(N)]

for _ in range(M):
    u, v = map(int, input().split())
    g[u - 1].append(v - 1)
    g[v - 1].append(u - 1)

seen = [False] * N
ans = 0
def dfs(g, v, n):
    global ans
    seen[v] = True
    if n == N:
        ans += 1
        return
    for nx in g[v]:
        if seen[nx]:
            continue
        dfs(g, nx, n + 1)
        seen[nx] = False

dfs(g, 0, 1)
print(ans)