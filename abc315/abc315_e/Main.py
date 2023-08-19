N = int(input())
g = [[] for _ in range(N)]
CP = [list(map(int, input().split())) for _ in range(N)]
C = []
for i in range(N):
    C.append(CP[i][0])
    for j in range(1, CP[i][0] + 1):
        g[i].append(CP[i][j] - 1)

import sys
sys.setrecursionlimit(10 ** 6)
seen = [False] * N
ans = []
def dfs(v):
    seen[v] = True
    for nx in g[v]:
        if seen[nx]:
            continue
        dfs(nx)
        ans.append(nx + 1)

dfs(0)
print(*ans)