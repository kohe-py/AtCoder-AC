import sys 
sys.setrecursionlimit(300000)

N = int(input())
G = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)

for i in range(N):
    G[i].sort()

result = []
def dfs(now, pre):
    result.append(now+1)
    for next_to in G[now]:
        if next_to != pre:
            dfs(next_to, now)
            result.append(now+1)

dfs(0, -1)
print(*result)