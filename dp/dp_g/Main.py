from collections import deque

N, M = map(int, input().split())
G = [[] * (N) for _ in range(N)]
input_order = [0] * N
for _ in range(M):
    x, y = map(int, input().split())
    input_order[y-1] += 1
    G[x-1].append(y-1)
#print(G)

def topo_sort(G, a, N):
    q = deque()
    for i in range(N):
        if a[i]==0:
            q.append(i)
    
    #幅
    ans = []
    while q:
        v = q.popleft()
        ans.append(v)
        for g in G[v]:
            a[g] -= 1
            if a[g]==0:
                q.append(g)
    
    return ans

#print(topo_sort(G, input_order, N))
topo = topo_sort(G, input_order, N)
dp = [-10**9] * N
for i in range(N):
    if input_order[i] == 0:
        dp[i] = 0

for n in topo:
    for v in G[n]:
        dp[v] = max(dp[v], dp[n] + 1)
print(max(dp))