from collections import deque

#入力
N, M = map(int, input().split())
G = [[] * N for _ in range(N)]
for _ in range(M):
    x, y = map(int, input().split())
    G[x-1].append(y-1)
    G[y-1].append(x-1)
    
def search(G, N, s):
    count = 0
    #seen = [False] * N
    todo = deque()
    
    seen[s] = True
    todo.append(s)
    
    while len(todo) != 0:
        v = todo.popleft()
        for n in G[v]:
            if seen[n]:
                continue
            else:
                seen[n] = True
                todo.append(n)


ans = 0
seen = [False] * N
for i in range(N):
    if seen[i]:
        continue        
    else:
        search(G, N, i)
        ans += 1
print(ans)