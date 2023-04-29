from collections import defaultdict, deque
import sys
sys.setrecursionlimit(10**8)

N, X, Y = map(int, input().split())
g = [[] for _ in range(N)]
for _ in range(N-1):
    u, v = map(int, input().split())
    g[u-1].append(v-1)
    g[v-1].append(u-1)

prev = [-1] * N
def dfs(g, s, pre):
    for n in g[s]:
        if n == pre:
            continue
        else:
            prev[n] = s 
            dfs(g, n, s)

                
s = X-1
now = Y-1
dfs(g, s, -1)
path = deque()
path.append(Y)
while prev[now] != -1:
    now = prev[now]
    path.append(now + 1)
    
path = reversed(path)
print(*path)