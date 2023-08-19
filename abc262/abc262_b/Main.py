N, M = map(int, input().split())
g = [set() for _ in range(N)]
ans = 0
for _ in range(M):
    u, v = map(int, input().split())
    g[u - 1].add(v - 1)
    g[v - 1].add(u - 1)
    for i in g[u - 1]:
        if i in g[v - 1]:
            ans += 1
print(ans)