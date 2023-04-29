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
    
    color[s] = 0
    todo.append(s)
    
    flag = True
    while len(todo) != 0:
        v = todo.popleft()
        for n in G[v]:
            if color[n] != -1:
                if color[n] == color[v]:
                    flag = False
                    continue
            else:
                color[n] = 1 - color[v]
                todo.append(n)
    return flag

color = [-1] * N
flag = True
for i in range(N):
    if color[i] != -1:
        continue
    else:
        if search(G, N, i) == False:
            print("No")
            exit()
            
print("Yes")