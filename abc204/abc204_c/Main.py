from collections import defaultdict, deque
N, M = map(int, input().split())
g = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    g[a-1].append(b-1)

ans = 0
for i in range(N):
    todo = deque()
    visit = set()
    visit.add(i)
    todo.append(i)
    while len(todo) != 0:
        edge = todo.popleft()
        for v in g[edge]:
            if v not in visit:
                todo.append(v)
                visit.add(v)
    ans += len(visit)
    #print(len(visit), visit)

print(ans)