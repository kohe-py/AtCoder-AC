N, M = map(int, input().split())
g = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    g[u - 1].append(v - 1)
    g[v - 1].append(u - 1)


from collections import deque, defaultdict
seen = [False] * N
per = [-1] * N
def DFS(s):
    d = defaultdict(set)
    flag = True
    todo = deque()
    todo.append(s)
    seen[s] = True
    while todo:
        v = todo.pop()
        for nx in g[v]:
            if seen[nx] == False:
                seen[nx] = True
                todo.append(nx)
                per[nx] = v
            else:
                if per[v] != nx:
                    flag = False 
    return flag

count = 0
for i in range(N):
    #print(seen)
    if seen[i]:
        #print(i)
        continue
    else:
        if DFS(i):
            #print(i)
            count += 1

print(count)