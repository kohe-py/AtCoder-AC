from collections import defaultdict
import heapq
N, M = map(int, input().split())

g = [[] for _ in range(N)]
w = defaultdict(int)
S = 0

for _ in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    S += max(0, c)
    g[a].append((c, b))
    g[b].append((c, a))

ans = 0
edge = 0
visit = set()
todo = [(0, 0)]
heapq.heapify(todo)
#print(g)
while todo:
    cost, v = heapq.heappop(todo)
    #print(cost, v)
    if v in visit:
        continue

    edge += 1
    visit.add(v)
    ans += max(0, cost)
    for c, nx in g[v]:
        if nx not in visit:
            heapq.heappush(todo, (c, nx))
    if edge == N:
        break
#print(ans, S)
print(S - ans)