from collections import defaultdict, deque
N = int(input())
graph = defaultdict(list)
for i in range(N):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

#print(graph)
que = deque()
que.append(1)
S = {1}
while que:
    x = que.popleft()
    for i in range(len(graph[x])):
        if graph[x][i] not in S:
            que.append(graph[x][i])
            S.add(graph[x][i])

print(max(S))